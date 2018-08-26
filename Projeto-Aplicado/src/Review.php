<?php
/**
 * Created by PhpStorm.
 * User: alexander
 * Date: 26/08/18
 * Time: 13:04
 */

namespace App;


class Review
{
    private $author;
    private $authorLink;
    private $date;

    /**
     * @return mixed
     */
    public function getAuthor()
    {
        return $this->author;
    }

    /**
     * @param mixed $author
     */
    public function setAuthor($author)
    {
        $this->author = $author;
    }

    /**
     * @return mixed
     */
    public function getAuthorLink()
    {
        return $this->authorLink;
    }

    /**
     * @param mixed $authorLink
     */
    public function setAuthorLink($authorLink)
    {
        $this->authorLink = $authorLink;
    }

    /**
     * @return mixed
     */
    public function getDate()
    {
        return $this->date;
    }

    /**
     * @param mixed $date
     */
    public function setDate($date)
    {
        $this->date = $date;
    }

    /**
     * @return mixed
     */
    public function getOpinion()
    {
        return $this->opinion;
    }

    /**
     * @param mixed $opinion
     */
    public function setOpinion($opinion)
    {
        $this->opinion = $opinion;
    }

    /**
     * @return mixed
     */
    public function getComment()
    {
        return $this->comment;
    }

    /**
     * @param mixed $comment
     */
    public function setComment($comment)
    {
        $this->comment = $comment;
    }
    private $opinion;
    private $comment;
}