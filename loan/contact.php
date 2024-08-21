<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $name = htmlspecialchars($_POST['name']);
    $email = htmlspecialchars($_POST['email']);
    $message = htmlspecialchars($_POST['message']);

    // 이메일 내용 작성
    $to = "your-email@example.com";
    $subject = "상담 문의: $name";
    $body = "이름: $name\n이메일: $email\n문의 내용:\n$message";
    $headers = "From: $email";

    // 이메일 보내기
    if (mail($to, $subject, $body, $headers)) {
        echo "문의가 성공적으로 접수되었습니다.";
    } else {
        echo "문의 접수에 실패하였습니다. 다시 시도해주세요.";
    }
}
?>
