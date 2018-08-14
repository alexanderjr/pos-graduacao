<?php
    use App\CrawlerFoursquare;
    use Symfony\Component\DomCrawler\Crawler;

    error_reporting(E_ALL);
    ini_set('display_errors', 1);

    require "vendor/autoload.php";

    #https://towardsdatascience.com/building-a-recommendation-system-for-fragrance-5b00de3829da

    $client = new GuzzleHttp\Client();
    $result = $client->request('GET', 'https://pt.foursquare.com/v/aqu%C3%A1rio-de-s%C3%A3o-paulo/4b51d04af964a520845627e3?tipsSort=recent');

    if($result->getStatusCode() == 200)
    {
        $html = $result->getBody();
    }
    else
    {
        echo $result->getStatusCode();
    }

