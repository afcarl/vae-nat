import numpy as np

import batching_functions


def test_random_batching():
    points = np.random.uniform(size=(10, 2))
    batching_function = batching_functions.random_batching(points)

    a, b = batching_function(5, points, {}), batching_function(5, points, {})
    # check that this is the whole dataset
    epoch_indices = np.concatenate((a, b)).tolist()
    assert len(epoch_indices) == 10
    assert len(epoch_indices) == len(set(epoch_indices))
    assert set(epoch_indices) == set(range(10))

    batches = [batching_function(2, points, {}) for _ in range(5)]
    assert all(len(batch) == 2 for batch in batches)
    epoch_indices2 = np.concatenate(batches).tolist()

    assert set(epoch_indices2) == set(epoch_indices)


def test_progressive_local_search():
    # TODO: proper testing other than covering the code
    points = np.random.uniform(size=(10, 2))
    batching_function = batching_functions.progressive_local_search(points)

    for i in range(200):
        batching_function(batch_size=10, context={'current_step': i}, targets=points)