import unittest

from recommend import search, rate_all,best_predictor, find_predictor, make_restaurant, make_review, group_by_centroid, find_closest, find_centroid, k_means
from abstractions import restaurant_price, make_user, make_review, make_restaurant,restaurant_ratings, restaurant_name, restaurant_num_ratings, restaurant_mean_rating

class Test_test1(unittest.TestCase):

    r1 = 0
    r2 = 0
    r3 = 0
    r4 = 0
    r5 = 0
    c1 = 0
    c2 = 0
    restaurants1 = 0
    restaurants2 =0



    def test_restaurant_ratings(self):
        soda_reviews = [make_review('Soda', 4.5),
                make_review('Soda', 4)]
        soda = make_restaurant('Soda', [127.0, 0.1],
                       ['Restaurants', 'Breakfast & Brunch'],
                       1, soda_reviews)
        val =restaurant_ratings(soda)
        self.assertEqual(val,[4.5, 4])

    def test_restaurant_num_ratings(self):
        woz_reviews = [make_review('Wozniak Lounge', 4),
               make_review('Wozniak Lounge', 3),
               make_review('Wozniak Lounge', 5)]
        woz = make_restaurant('Wozniak Lounge', [127.0, 0.1],
                      ['Restaurants', 'Pizza'],
                      1, woz_reviews)
        val = restaurant_num_ratings(woz)
        self.assertEqual(val,3)

    def test_restaurant_mean_rating(self):
        woz_reviews = [make_review('Wozniak Lounge', 4),
               make_review('Wozniak Lounge', 3),
               make_review('Wozniak Lounge', 5)]
        woz = make_restaurant('Wozniak Lounge', [127.0, 0.1],
                      ['Restaurants', 'Pizza'],
                      1, woz_reviews)
        val = restaurant_mean_rating(woz)
        self.assertEqual(val,4.0)

    def test_find_closest_1(self):
        val = find_closest([6, 1], [[1, 5], [3, 3]])
        self.assertEqual(val,[3, 3])

    def test_find_closest_2(self):
        val = find_closest([1, 6], [[1, 5], [3, 3]])
        self.assertEqual(val,[1, 5])

    def test_find_closest_3(self):
        val = find_closest([0, 0], [[-2, 0], [2, 0]])
        self.assertEqual(val,[-2, 0])

    def test_find_closest_4(self):
        val = find_closest([0, 0], [[1000, 1000]])
        self.assertEqual(val,[1000, 1000])

    def test_find_centroid(self):
        cluster1 = [
            make_restaurant('A', [-3, -4], [], 3, [make_review('A', 2)]),
            make_restaurant('B', [1, -1],  [], 1, [make_review('B', 1)]),
            make_restaurant('C', [2, -4],  [], 1, [make_review('C', 5)]),
            ]
        val = find_centroid(cluster1) # should be a pair of decimals
        self.assertEqual(val,[0.0, -3.0])

    def test_group_by_centroid(self):
        print("test1")
        print(self.r1)
        groups = group_by_centroid([self.r1, self.r2, self.r3, self.r4, self.r5], [self.c1, self.c2])
        # correct grouping is  [[r1, r2], [r3, r4, r5]])
        val = [list (map (lambda r: r ['name'], c)) for c in groups]
        self.assertEqual(val,[['A', 'B'], ['C', 'D', 'E']])

    def test_kmeans1(self):
        centroids = k_means(self.restaurants1, 1)
        self.assertEqual(centroids,[[0.0, -3.0]])

    def test_kmeans2(self):
        centroids = k_means(self.restaurants2, 1)
        self.assertEqual(centroids,[[1.0, 3.0]])

    def test_kmeans3(self):
        centroids = k_means(self.restaurants1 + self.restaurants2, 1)
        centroids.sort(key=lambda tup: tup[0]+tup[1])
        self.assertEqual(centroids,[[0.4, -0.6]])

    def test_kmeans4(self):
        centroids = k_means(self.restaurants1 + self.restaurants2, 2)
        centroids.sort(key=lambda tup: tup[0]+tup[1])
        self.assertEqual(centroids,[[0.0, -3.0], [1.0, 3.0]])

    def test_kmeans5(self):
        centroids = k_means(self.restaurants1 + self.restaurants2, 3)
        centroids.sort(key=lambda tup: tup[0]+tup[1])
        self.assertEqual(centroids,[[-0.5, -4.0], [1.0, -1.0], [1.0, 3.0]])

    def test_kmeans6(self):
        centroids = k_means(self.restaurants1 + self.restaurants2, 4)
        centroids.sort(key=lambda tup: tup[0]+tup[1])
        self.assertEqual(centroids,[[-3.0, -4.0],[1.5, -2.5], [0.0, 3.0],  [2.0, 3.0]])

    def test_kmeans7(self):
        centroids = k_means(self.restaurants1 + self.restaurants2, 5)
        centroids.sort(key=lambda tup: tup[0]+tup[1])
        self.assertEqual(centroids,[[-3.0, -4.0], [2.0, -4.0], [1.0, -1.0], [0.0, 3.0], [2.0, 3.0]])

    def test_find_predictor(self):
        user = make_user('John D.', [
            make_review('A', 1),
            make_review('B', 5),
            make_review('C', 2),
            make_review('D', 2.5),])
        restaurant = make_restaurant('New', [-10, 2], [], 2, [make_review('New', 4),])
        cluster = [make_restaurant('B', [4, 2], [], 1, [make_review('B', 5)]),
            make_restaurant('C', [-2, 6], [], 4, [make_review('C', 2)]),
            make_restaurant('D', [4, 2], [], 3.5, [make_review('D', 2.5),
                make_review('D', 3),]),]
        pred, r_squared = find_predictor(user, cluster, restaurant_mean_rating)
        val1 = round(pred(restaurant), 5)
        print("val1 is: "+str(val1))
        self.assertAlmostEqual(val1, 3.9359,4)
        val2 = round(r_squared, 5)
        print("val2 is: "+str(val2))
        self.assertAlmostEqual(val2, 0.99256,4)

    def test_best_predictor(self):
        user = make_user('Cheapskate', [
         make_review('A', 2),
         make_review('B', 5),
         make_review('C', 2),
         make_review('D', 5),
        ])

        cluster = [
            make_restaurant('A', [5, 2], [], 4, [
            make_review('A', 5) ]),
            make_restaurant('B', [3, 2], [], 2, [
            make_review('B', 5) ]),
            make_restaurant('C', [-2, 6], [], 4, [
            make_review('C', 4) ]), ]

        fns = [restaurant_price, restaurant_mean_rating]

        pred = best_predictor(user, cluster, fns)
        print ([round(pred(r), 5) for r in cluster], "SHOULD =",[2.0, 5.0, 2.0])
        self.assertEqual([round(pred(r), 5) for r in cluster], [2.0, 5.0, 2.0])

    def test_rate_all(self):
        user = make_user('Mr. Mean Rating Minus One', [make_review('A', 3),make_review('B', 4), make_review('C', 1),])

        cluster = [make_restaurant('A', [1, 2], [], 4, 
        [make_review('A', 4), make_review('A', 4) ]),
        make_restaurant('B', [4, 2], [], 3, [make_review('B', 5)]),
        make_restaurant('C', [-2, 6], [], 4, [make_review('C', 2) ]),
        make_restaurant('D', [4, 4], [], 3.5, [
        make_review('D', 2.5), make_review('D', 3.5), ]),]

        restaurants = {restaurant_name(r): r for r in cluster}

        ALL_RESTAURANTS = cluster

        to_rate = cluster[2:]

        fns = [restaurant_price, restaurant_mean_rating]

        ratings = rate_all(user, to_rate, fns,ALL_RESTAURANTS)
        print(type(ratings), "Should be ", "dict")

        print(len(ratings), "Should be ",  2)

        print(ratings['C'], "Should be", 1)
        self.assertEqual(ratings['C'],1)
        print(round(ratings['D'], 5), "Should be ", 2.0)
        self.assertEqual(ratings['D'],2.0)

    def test_search(self):
        val = search('Thai', [self.r1, self.r2, self.r3, self.r4, self.r5])
        print(val,'==', ['A','D'])
        self.assertEqual(val, ['A','D'])

    def setUp(self):
        print("setUp")


    def tearDown(self):
        print("tearDown")

    @classmethod
    def setUpClass(cls):
        print("setUpClass")
        cls.r1 = make_restaurant('A', [-10, 2], ['Fast Food','Thai'], 2, [make_review('A', 4),])
        cls.r2 = make_restaurant('B', [-9, 1], ['Fast Food','American'], 3, [make_review('B', 5),make_review('B', 3.5),])
        cls.r3 = make_restaurant('C', [4, 2], ['Fast Food',], 1, [make_review('C', 5) ])
        cls.r4 = make_restaurant('D', [-2, 6], ['Sit Down','Thai'], 4, [make_review('D', 2)])
        cls.r5 = make_restaurant('E', [4, 2], ['Italian','German'], 3.5, [make_review('E', 2.5), make_review('E', 3),])
        cls.c1 = [0, 0]
        cls.c2 = [3, 4]
        cls.restaurants1 = [
            make_restaurant('A', [-3, -4], [], 3, [make_review('A', 2)]),
            make_restaurant('B', [1, -1],  [], 1, [make_review('B', 1)]),
            make_restaurant('C', [2, -4],  [], 1, [make_review('C', 5)])]

        cls.restaurants2 = [
            make_restaurant('D', [2, 3], [], 2, [make_review('D', 2)]),
            make_restaurant('E', [0, 3], [], 3, [make_review('E', 1)])]

    @classmethod
    def tearDownClass(cls):
        print("tearDownClass")

if __name__ == '__main__':
    unittest.main()
