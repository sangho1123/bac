import pandas as pd
from openpyxl import Workbook
from openpyxl.utils.dataframe import dataframe_to_rows
import win32com.client as win32

# 데이터 생성
data = {
    "Year": [2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023],
    "Profit": [512508112, 394509738, 364401168, 337566358, 291023905, 280261974, 321112180, 302249519, 287418964, 243010565, 105056700, 233388925, 186026376, -39776206]
}

df = pd.DataFrame(data)

# 워크북 및 워크시트 생성
wb = Workbook()
ws = wb.active
ws.title = "Data"

# 데이터프레임을 워크시트에 작성
for r in dataframe_to_rows(df, index=False, header=True):
    ws.append(r)

# 임시 파일로 저장 (바탕 화면 경로 사용)
temp_file_path = r"C:\Users\sanghojeong9210\Desktop\temp_poly.xlsx"
wb.save(temp_file_path)

# VBA 매크로 코드 정의
vba_code = """
Function PolynomialRegressionPredict(xValues As Range, yValues As Range, degree As Integer, predictYear As Double) As Double
    Dim i As Integer, j As Integer
    Dim n As Integer
    Dim X() As Double, Y() As Double
    Dim XMatrix() As Double, YMatrix() As Double
    Dim A() As Double, B() As Double

    n = xValues.Rows.Count
    ReDim X(1 To n)
    ReDim Y(1 To n)
    ReDim XMatrix(1 To n, 1 To degree + 1)
    ReDim YMatrix(1 To n, 1 To 1)

    ' Load the data into arrays
    For i = 1 To n
        X(i) = xValues.Cells(i, 1).Value
        Y(i) = yValues.Cells(i, 1).Value
        For j = 1 To degree + 1
            XMatrix(i, j) = X(i) ^ (j - 1)
        Next j
        YMatrix(i, 1) = Y(i)
    Next i

    ' Perform the matrix calculations
    Dim XTX() As Double
    Dim XTY() As Double
    Dim XTXInverse() As Double

    XTX = Application.MMult(Application.Transpose(XMatrix), XMatrix)
    XTY = Application.MMult(Application.Transpose(XMatrix), YMatrix)
    XTXInverse = Application.MInverse(XTX)
    A = Application.MMult(XTXInverse, XTY)

    ' Calculate the predicted value
    Dim predictX() As Double
    ReDim predictX(1 To degree + 1)

    For i = 1 To degree + 1
        predictX(i) = predictYear ^ (i - 1)
    Next i

    PolynomialRegressionPredict = Application.MMult(Application.Transpose(A), Application.Transpose(predictX))
End Function
"""

# 엑셀 애플리케이션 시작
excel = win32.gencache.EnsureDispatch('Excel.Application')
excel.Visible = False

try:
    # 엑셀 파일 열기
    wb = excel.Workbooks.Open(temp_file_path)

    # VBA 모듈 추가
    vb_module = wb.VBProject.VBComponents.Add(1)  # 1 corresponds to a standard module
    vb_module.CodeModule.AddFromString(vba_code)

    # 매크로가 포함된 파일로 저장
    file_path = r"C:\Users\sanghojeong9210\Desktop\업무\_Credit모델\Cash_Forecast\poly.xlsm"
    wb.SaveAs(file_path, FileFormat=52)  # 52 corresponds to the xlsm format

    print(f"File saved as {file_path}")

finally:
    # 엑셀 애플리케이션 종료
    wb.Close(SaveChanges=True)
    excel.Application.Quit()
