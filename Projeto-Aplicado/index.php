    <?php
    use App\CrawlerFoursquare;
    use App\Review;
    use Symfony\Component\DomCrawler\Crawler;

    error_reporting(E_ALL);
    ini_set('display_errors', 1);

    require "vendor/autoload.php";

    #https://towardsdatascience.com/building-a-recommendation-system-for-fragrance-5b00de3829da


    $html = file_get_contents("file.txt");
    $crawler = new Crawler($html);

    $obj = new CrawlerFoursquare();

    $obj->setName($crawler->filter('[itemprop="name"]')->text());
    $obj->setType($crawler->filter('.unlinkedCategory')->text());
    $obj->setCity($crawler->filter('[itemprop="addressLocality"]')->text());
    $obj->setState($crawler->filter('[itemprop="addressRegion"]')->text());
    $obj->setZipCode($crawler->filter('[itemprop="postalCode"]')->text());
    $obj->setQtyReviews($crawler->filter('.numRatings')->text());
    $obj->setMeanReviews($crawler->filter('[itemprop="ratingValue"]')->text());
    $obj->setAddress($crawler->filter('[itemprop="streetAddress"]')->text());
    //$obj->setOpenHours($crawler->filter('XXXXX')->text());
    $obj->setLinkFacebook($crawler->filter('.facebookPageLink')->text());
    $obj->setWebsite($crawler->filter('[itemprop="url"]')->text());

    $tags = [];

    foreach($crawler->filter('.tastePile li') as $dom)
    {
        $tags[] = $dom->textContent;
    }

    $obj->setTags($tags);
    $obj->setTelephone($crawler->filter('[itemprop="telephone"]')->text());

    $crawler->filter('#tipsList li')->each(function(Crawler $dom, $i) use($obj){
        $review = new Review();
        $review->setAuthor($dom->filter('.tipContents .userName')->text());
        $review->setAuthorLink($dom->filter('.tipContents .userName a')->attr('href'));
        $review->setDate($dom->filter('.tipContents .tipDate')->text());
        $review->setComment($dom->filter('.tipContents .tipText')->text());
        $review->setOpinion(0);

        if($dom->filter('.authorImage .tipAuthorInteractionIcon')->count())
        {
            $temp = $dom->filter('.authorImage .tipAuthorInteractionIcon')->attr('src');

            if(strpos($temp, "tip_like" ) > 0)
            {
                $review->setOpinion(1);
            }

            if(strpos($temp, "tip_dislike" ) > 0)
            {
                $review->setOpinion(-1);
            }

        }

        $obj->setReviews($review);

    });

    $obj->print();

    exit;

    $client = new GuzzleHttp\Client();
    $result = $client->request('GET', 'https://pt.foursquare.com/v/aqu%C3%A1rio-de-s%C3%A3o-paulo/4b51d04af964a520845627e3?tipsSort=recent');

    if($result->getStatusCode() == 200)
    {
        $html = $result->getBody();
        file_put_contents("file.txt", $html);
        $crawler = new Crawler($html);
        //echo $crawler->filter('title');
        echo $html;
    }
    else
    {
        echo $result->getStatusCode();
    }

