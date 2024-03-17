<?php
    // Update the path below to your autoload.php,
    // see https://getcomposer.org/doc/01-basic-usage.md
    require_once '/path/to/vendor/autoload.php';
    use Twilio\Rest\Client;

    $sid    = "AC5a953573c0999dfab2a450e69b217087";
    $token  = "e1a184007df0d6347c6c5f4341bbe280";
    $twilio = new Client($sid, $token);

    $message = $twilio->messages
      ->create("+254793260190", // to
        array(
          "from" => "+14433419871",
          "body" => MADE BY STEEN
        )
      );

print($message->sid);