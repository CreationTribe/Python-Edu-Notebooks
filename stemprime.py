# GENERAL NOTES
#...................................................

# alt linear functions def:
# wx+b
# xw+b
# x^tw+b
# w^tx+b

# Big-O Notation (Landau Notation)
#
# f(x) = O(g(x)) as x -> inf
#
# 1)  only if there is a positive constant 'c'
# such that FOR all sufficiently large values of 'x'
# the abs val of x is at most c*|g(x)|
#
# 2) if f(x) is a sum of multiple terms, the one
# with the largest growth rate is kept and the rest
# omitted. O(N+logN)=O(N)
#
# 3) if f(x) is a product of multiple factors,
# any constants are omitted O(c*N)=O(N)

# ::Sorting Algorithms Time Complexity::
# Big O Complexity
# factorial: O(N!)
# fewer elements, more operations
#
# Exponential: O(2^N)
# next fewer operations, more elements
#
# Quadratic: O(N^2)
# next fewer ops, more elems
#
# Linearithmic: O(N*logN)
# next fewer ops, more elems
#
# Linear: O(N)
# next fewer ops, more elems
#
# Logarithmic: O(logN)
# next fewer ops, more elems
#
# Constant: O(1)
# ops is constant

# Complexity Classes
# P (Polinomial)
# NP (Nondeterministic Polynomial)
# NP Complete (both NP and NP-Hard)
# NP-Hard ()


# THOMAS' NOTES:
# TF env: py3-TF2.0
# we're going to have to mix a bunch of different machine learning styles
# what we really need to figure out is how to convert and then transfer different
# model learning states across our supervised (specifically the classification models,
# the regression models are no biggie), and reinforcement models.
# So far, I think we' only need to go one way.
# The unsupervised models need to be able to check themselves against prepared states sent
# down from the meta-node's so we don't lose coherence.
#

# C.T.'s NOTES:
#

# MATT'S NOTES:
# 3 TYPES OF MACHINE LEARNING
# 1) supervised: prelabled samples
#     1) classification: outputs are categories
#     2) regression: outputs are numerical
# 2) unsupervised: not prelabled/algorithm finds differences
# 3) reinforcement: reward alg w/ score

