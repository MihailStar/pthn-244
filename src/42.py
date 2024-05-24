from dataclasses import dataclass, field

UserId = int
TweetId = int

_tweet_counter = 0


@dataclass
class _Tweet:
    tweet_id: TweetId
    created_at: int = field(init=False)

    def __post_init__(self) -> None:
        global _tweet_counter
        _tweet_counter += 1

        self.created_at = _tweet_counter


@dataclass
class _User:
    user_id: UserId
    tweets: list[_Tweet] = field(default_factory=list)
    following_ids: set[UserId] = field(default_factory=set)


class Twitter:
    _users: dict[UserId, _User]

    def __init__(self) -> None:
        self._users = dict()

    def _get_user(self, user_id: UserId) -> _User:
        if user_id not in self._users:
            self._users[user_id] = _User(user_id)

        return self._users[user_id]

    def post_tweet(self, user_id: UserId, tweet_id: TweetId) -> None:
        user = self._get_user(user_id)
        tweet = _Tweet(tweet_id)

        user.tweets.append(tweet)

    def get_news_feed(self, user_id: UserId) -> list[TweetId]:
        user = self._get_user(user_id)

        news_feed: list[_Tweet] = list()

        for following_id in user.following_ids:
            news_feed += self._get_user(following_id).tweets

        return list(
            map(
                lambda t: t.tweet_id,
                sorted(news_feed, key=lambda t: t.created_at, reverse=True)[:10],
            )
        )

    def follow(self, follower_id: UserId, followee_id: UserId) -> None:
        user = self._get_user(follower_id)

        user.following_ids.add(followee_id)

    def unfollow(self, follower_id: UserId, followee_id: UserId) -> None:
        user = self._get_user(follower_id)

        try:
            user.following_ids.remove(followee_id)
        except KeyError:
            ...
