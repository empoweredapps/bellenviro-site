<?php
// Bell Enviro contact form handler. Sends to $to via PHP mail(); honeypot + timing spam checks.
$to      = 'chris@bellenviro.au';
$from    = 'noreply@bellenviro.au';   // must be a mailbox/domain on this cPanel account
$subject = 'Website enquiry';

if ($_SERVER['REQUEST_METHOD'] !== 'POST') { header('Location: /contact/'); exit; }

$f = fn($k, $max = 4000) => trim(mb_substr((string)($_POST[$k] ?? ''), 0, $max));
$name = $f('name', 100); $company = $f('company', 100); $email = $f('email', 150); $phone = $f('phone', 40);
$service = $f('service', 100); $location = $f('location', 150); $message = $f('message'); $hp = $f('website'); $ts = (int)$f('ts', 20);

// Spam checks: honeypot filled, or form submitted in under 3 seconds, or no JS timestamp
if ($hp !== '' || $ts === 0 || (microtime(true) * 1000 - $ts) < 3000) { header('Location: /thanks/'); exit; }
if ($name === '' || $message === '' || !filter_var($email, FILTER_VALIDATE_EMAIL)) { header('Location: /contact/?error=1'); exit; }
if (preg_match('/[\r\n]/', $name . $email)) { exit; } // header injection guard

$body = "New enquiry from bellenviro.au\n\n"
      . "Name:     $name\nCompany:  $company\nEmail:    $email\nPhone:    $phone\n"
      . "Service:  $service\nLocation: $location\n\nMessage:\n$message\n\n"
      . "IP: " . ($_SERVER['REMOTE_ADDR'] ?? '') . "\nTime: " . date('c') . "\n";

$headers = "From: Bell Enviro Website <$from>\r\nReply-To: $name <$email>\r\nContent-Type: text/plain; charset=UTF-8\r\n";
@mail($to, "$subject: $service — $name", $body, $headers, "-f$from");
header('Location: /thanks/');
exit;
