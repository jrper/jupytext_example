# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.15.2
# ---

# %% [markdown]
# # An example notebook to demonstrate jupytext

# %%
# A sorting algorithm

def sort(arr):
    """An implementation of the bubble sort algorithm.

    Bubble sort is a simple(often quite bad) sorting algorithm.

    Parameters
    ----------
    arr : array_like
        The sequence to be sorted.

    Returns
    -------
    arr : array_like
        The (inplace) sorted sequence.
    """
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]

    return arr
