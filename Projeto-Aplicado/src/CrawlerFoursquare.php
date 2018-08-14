<?php

namespace App;

class CrawlerFoursquare
{
    private $name;
    private $type;
    private $city;
    private $state;
    private $tips;
    private $qtyReviews;
    private $meanReviews;
    private $address;
    private $openHours;
    private $linkFacebook;
    private $website;
    private $tags;
    private $extras;
    private $telephone;
    private $reviews;

    /**
     * @return mixed
     */
    public function getName()
    {
        return $this->name;
    }

    /**
     * @param mixed $name
     * @return CrawlerFoursquare
     */
    public function setName($name)
    {
        $this->name = $name;
        return $this;
    }

    /**
     * @return mixed
     */
    public function getType()
    {
        return $this->type;
    }

    /**
     * @param mixed $type
     * @return CrawlerFoursquare
     */
    public function setType($type)
    {
        $this->type = $type;
        return $this;
    }

    /**
     * @return mixed
     */
    public function getCity()
    {
        return $this->city;
    }

    /**
     * @param mixed $city
     * @return CrawlerFoursquare
     */
    public function setCity($city)
    {
        $this->city = $city;
        return $this;
    }

    /**
     * @return mixed
     */
    public function getState()
    {
        return $this->state;
    }

    /**
     * @param mixed $state
     * @return CrawlerFoursquare
     */
    public function setState($state)
    {
        $this->state = $state;
        return $this;
    }

    /**
     * @return mixed
     */
    public function getTips()
    {
        return $this->tips;
    }

    /**
     * @param mixed $tips
     * @return CrawlerFoursquare
     */
    public function setTips($tips)
    {
        $this->tips = $tips;
        return $this;
    }

    /**
     * @return mixed
     */
    public function getQtyReviews()
    {
        return $this->qtyReviews;
    }

    /**
     * @param mixed $qtyReviews
     * @return CrawlerFoursquare
     */
    public function setQtyReviews($qtyReviews)
    {
        $this->qtyReviews = $qtyReviews;
        return $this;
    }

    /**
     * @return mixed
     */
    public function getMeanReviews()
    {
        return $this->meanReviews;
    }

    /**
     * @param mixed $meanReviews
     * @return CrawlerFoursquare
     */
    public function setMeanReviews($meanReviews)
    {
        $this->meanReviews = $meanReviews;
        return $this;
    }

    /**
     * @return mixed
     */
    public function getAddress()
    {
        return $this->address;
    }

    /**
     * @param mixed $address
     * @return CrawlerFoursquare
     */
    public function setAddress($address)
    {
        $this->address = $address;
        return $this;
    }

    /**
     * @return mixed
     */
    public function getOpenHours()
    {
        return $this->openHours;
    }

    /**
     * @param mixed $openHours
     * @return CrawlerFoursquare
     */
    public function setOpenHours($openHours)
    {
        $this->openHours = $openHours;
        return $this;
    }

    /**
     * @return mixed
     */
    public function getLinkFacebook()
    {
        return $this->linkFacebook;
    }

    /**
     * @param mixed $linkFacebook
     * @return CrawlerFoursquare
     */
    public function setLinkFacebook($linkFacebook)
    {
        $this->linkFacebook = $linkFacebook;
        return $this;
    }

    /**
     * @return mixed
     */
    public function getWebsite()
    {
        return $this->website;
    }

    /**
     * @param mixed $website
     * @return CrawlerFoursquare
     */
    public function setWebsite($website)
    {
        $this->website = $website;
        return $this;
    }

    /**
     * @return mixed
     */
    public function getTags()
    {
        return $this->tags;
    }

    /**
     * @param mixed $tags
     * @return CrawlerFoursquare
     */
    public function setTags($tags)
    {
        $this->tags = $tags;
        return $this;
    }

    /**
     * @return mixed
     */
    public function getExtras()
    {
        return $this->extras;
    }

    /**
     * @param mixed $extras
     * @return CrawlerFoursquare
     */
    public function setExtras($extras)
    {
        $this->extras = $extras;
        return $this;
    }

    /**
     * @return mixed
     */
    public function getTelephone()
    {
        return $this->telephone;
    }

    /**
     * @param mixed $telephone
     * @return CrawlerFoursquare
     */
    public function setTelephone($telephone)
    {
        $this->telephone = $telephone;
        return $this;
    }

    /**
     * @return mixed
     */
    public function getReviews()
    {
        return $this->reviews;
    }

    /**
     * @param mixed $reviews
     * @return CrawlerFoursquare
     */
    public function setReviews($reviews)
    {
        $this->reviews = $reviews;
        return $this;
    }
}