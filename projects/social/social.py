import random

from util import Queue


class User:
    def __init__(self, name):
        self.name = name


class SocialGraph:
    def __init__(self):
        self.last_id = 0
        self.users = {}
        self.friendships = {}

    def add_friendship(self, user_id, friend_id):
        """
        Creates a bi-directional friendship
        """
        if user_id == friend_id:
            print("WARNING: You cannot be friends with yourself")
        elif friend_id in self.friendships[user_id] or user_id in self.friendships[friend_id]:
            print("WARNING: Friendship already exists")
        else:
            self.friendships[user_id].add(friend_id)
            self.friendships[friend_id].add(user_id)

    def add_user(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.last_id += 1  # automatically increment the ID to assign the new user
        self.users[self.last_id] = User(name)
        self.friendships[self.last_id] = set()

    def populate_graph(self, num_users, avg_friendships):
        """
        Takes a number of users and an average number of friendships
        as arguments

        Creates that number of users and a randomly distributed friendships
        between those users.

        The number of users must be greater than the average number of friendships.
        """
        # Reset graph
        self.last_id = 0
        self.users = {}
        self.friendships = {}

        # !!!! IMPLEMENT ME
        # Add users
        for i in range(num_users):
            self.add_user(f"User {i+1}")

        # Create friendships
        possible_friendships = []
        # Avoid dups by ensuring the first ID is smaller than the second
        for user_id in self.users:
            for friend_id in range(user_id + 1, self.last_id + 1):
                possible_friendships.append((user_id, friend_id))

        # Shuffle the list
        random.shuffle(possible_friendships)
        print("Random Friendships:")
        print(possible_friendships)

        # Slice off total_friendships from the front, create friendships
        total_friendships = avg_friendships * num_users // 2
        print(f"Frienships to create: {total_friendships}\n")
        for i in range(total_friendships):
            friendship = possible_friendships[i]
            self.add_friendship(friendship[0], friendship[1])

    def get_all_social_paths(self, user_id):
        """
        Takes a user's user_id as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        visited = {}  # Note that this is a dictionary, not a set
        # !!!! IMPLEMENT ME
        for id in self.friendships:
            visited[id] = self.bfs_social(user_id, id)

        print(f"Visited all_social_paths: {visited}")
        return visited

    def bfs_social(self, starting_id, ending_id):
        # Create an empty queue
        queue = Queue()

        # Add starting id to queue
        queue.enqueue([starting_id])

        # Create an empty set for visited verts
        visited = set()

        while queue.size() > 0:
            path = queue.dequeue()
            v = path[-1]
            if v not in visited:
                # Check if v is target
                if v == ending_id:
                    # Return entire path
                    return path
                # Mark it as visited...
                visited.add(v)
                # Then add a path to it's neighbors to the beack of the queue
                for neighbor in self.friendships[v]:
                    copy = list(path)
                    # Append neighbor to the back
                    copy.append(neighbor)
                    queue.enqueue(copy)


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populate_graph(10, 2)
    print(sg.friendships)
    connections = sg.get_all_social_paths(1)
    print(connections)
