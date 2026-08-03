# Favour's AI & Computer Vision Learning Roadmap

A detailed, phase-by-phase course outline from advanced Python through to
Computer Vision specialization. Built around the **codebasics** roadmap,
running alongside the **DSN Deeptech Cohort 3** coursework.

Check items off as you go. Each phase lists *why it matters*, *what to learn*,
*practice*, and *where it lives in this repo*.

---

## Progress Snapshot

- [x] Phase 0 — Python Basics
- [ ] Phase 1 — Advanced Python (OOP) - done
- [ ] Phase 2 — Data Structures & Algorithms - in progress
- [ ] Phase 3 — Python for Data (NumPy / Pandas / Matplotlib)
- [ ] Phase 4 — Core Machine Learning
- [ ] Phase 5 — Deep Learning Foundations
- [ ] Phase 6 — Computer Vision Specialization
- [ ] Phase 7 — Projects & Portfolio

---

## Phase 0: Python Basics ✅ (done)

Variables, data types, strings, lists, conditionals, loops, `input()`.
Lives in [`python/basics.py`](./python/basics.py).

---

## Phase 1: Advanced Python (OOP)

**Why it matters:** Every ML/DL framework you'll touch (PyTorch, scikit-learn,
even OpenCV's newer APIs) is built and used through classes. `class MyModel(nn.Module)`
won't make sense until this is second nature.

**Topics, in order:**
- [ ] Functions deep dive: `*args`, `**kwargs`, default params, return values
- [ ] Classes & objects: `__init__`, instance attributes vs class attributes
- [ ] Methods vs static methods (`@staticmethod`) vs class methods (`@classmethod`)
- [ ] Inheritance: parent/child classes, `super()`
- [ ] Polymorphism & method overriding
- [ ] Encapsulation: public/protected/private (`_var`, `__var`) conventions
- [ ] Dunder/magic methods: `__str__`, `__repr__`, `__len__`, `__eq__`
- [ ] Exception handling: `try/except/finally`, custom exceptions
- [ ] File I/O: reading/writing files, `with` context managers
- [ ] Modules & packages: imports, `__init__.py` (you're already doing this in `image_processing_app/processors/`)
- [ ] List/dict comprehensions, generators, `lambda`
- [ ] Decorators (intro level — enough to read library code)

**Practice:** Build 2–3 small OOP programs (e.g. `BankAccount`, `Employee` hierarchy,
a simple `Shape` → `Circle`/`Rectangle` inheritance example) in
[`python/basics.py`](./python/basics.py) or a new `python/oop.py`.

**Estimated time:** 2–3 weeks, part-time.

---

## Phase 2: Data Structures & Algorithms

**Why it matters:** Interview prep, but also — writing efficient data pipelines
(image batching, augmentation loops) requires knowing *why* a list vs a set vs
a dict matters for performance.

**Topics, in order:**
- [ ] Big O notation (time & space complexity) — *you've already started this*
- [ ] Arrays & strings: two-pointer, sliding window patterns
- [ ] Hashing: dict/set, when and why they give O(1) lookup
- [ ] Recursion: base case, recursive case, tracing call stacks
- [ ] Searching: linear, binary search
- [ ] Sorting: bubble/selection (understand), merge/quick (understand + implement)
- [ ] Stacks & queues (+ where they show up: BFS, undo systems, parsing)
- [ ] Linked lists: singly, doubly, common interview patterns
- [ ] Trees: binary trees, BST, traversals (in/pre/post-order), BFS/DFS
- [ ] Graphs: representation (adjacency list/matrix), BFS/DFS, basic shortest path
- [ ] (Lighter touch) Dynamic programming: memoization, classic problems (fib, knapsack)

**Practice:** Solve 3–5 problems per topic on LeetCode/HackerRank (easy → medium).
Log solutions in [`python/DSA.py`](./python/DSA.py) with comments on time/space complexity.

**Estimated time:** 4–6 weeks, running in parallel with Phase 1 and Phase 3.

---

## Phase 3: Python for Data

**Why it matters:** Every ML/CV pipeline starts with data wrangling. You already
use NumPy/OpenCV in `image_preprocessing_technique/` — this phase formalizes it.

**Topics:**
- [ ] NumPy: arrays, broadcasting, vectorized ops, indexing/slicing (critical — images *are* NumPy arrays)
- [ ] Pandas: Series/DataFrame, filtering, groupby, merging, handling missing data
- [ ] Matplotlib / Seaborn: plotting distributions, images, training curves
- [ ] Reading/writing datasets (CSV, image folders, basic `torch`/`tf` datasets later)

**Practice:** Redo an image-preprocessing notebook explaining each NumPy op you use
(shape, dtype, axis) instead of just calling `cv2` functions.

**Estimated time:** 1–2 weeks (much of this overlaps what you already know from your CV app).

---

## Phase 4: Core Machine Learning

**Why it matters:** Before CNNs, you need the fundamentals — loss functions,
gradient descent, overfitting — or deep learning will feel like magic instead
of math you understand.

**Topics:**
- [ ] What is ML: supervised vs unsupervised, train/val/test splits
- [ ] Linear Regression (from scratch, then scikit-learn)
- [ ] Logistic Regression / classification basics
- [ ] Cost functions & Gradient Descent (ties back to your Coursera Math for ML)
- [ ] Overfitting/underfitting, regularization (L1/L2), bias-variance tradeoff
- [ ] Decision Trees, Random Forests (good intuition builders)
- [ ] Model evaluation: accuracy, precision/recall, F1, confusion matrix, ROC-AUC
- [ ] Feature scaling, one-hot encoding, basic feature engineering
- [ ] scikit-learn workflow: `fit`/`predict`/`pipeline`

**Practice:** One small end-to-end scikit-learn project (tabular dataset, not images yet)
to nail the workflow before jumping to DL.

**Estimated time:** 2–3 weeks.

---

## Phase 5: Deep Learning Foundations

**Why it matters:** This is the direct bridge to CV. You already have a CNN
notebook — this phase makes sure the *why* behind it is solid.

**Topics:**
- [ ] Perceptron → Multi-Layer Perceptron (MLP)
- [ ] Activation functions: sigmoid, ReLU, softmax — and why they matter
- [ ] Forward propagation & backpropagation (conceptual + by-hand example)
- [ ] Loss functions for DL: cross-entropy, MSE
- [ ] Optimizers: SGD, Momentum, Adam
- [ ] Framework fluency: PyTorch **or** TensorFlow/Keras (pick one; PyTorch is more common in CV research)
- [ ] `nn.Module`-style class-based model building (this is where Phase 1 OOP pays off directly)
- [ ] Training loop anatomy: epochs, batches, `optimizer.step()`, `loss.backward()`
- [ ] Convolutional Neural Networks: convolution, pooling, stride, padding, feature maps
- [ ] Regularization for DL: dropout, batch norm, data augmentation
- [ ] Transfer learning: fine-tuning pretrained models (ResNet, VGG, etc.)

**Practice:** Rebuild [`DL/notebook/cnn.ipynb`](./DL/notebook/cnn.ipynb) from scratch without
looking at the original, then compare — this reveals exactly what you don't yet own.

**Estimated time:** 3–4 weeks.

---

## Phase 6: Computer Vision Specialization

**Why it matters:** This is the destination — matches the goals already listed
in your [README](./README.md).

**Topics, in order:**
- [ ] Classic CV recap (you have a head start): filtering, edge detection, morphology,
      thresholding, segmentation — see [`image_preprocessing_technique/`](./image_preprocessing_technique)
- [ ] Image classification with CNNs (ResNet, EfficientNet architectures)
- [ ] Object detection: intuition → YOLO / Faster R-CNN
- [ ] Semantic & instance segmentation: U-Net, Mask R-CNN
- [ ] Vision Transformers (ViT) — architecture intuition, when they beat CNNs
- [ ] Model deployment basics: exporting models, serving via Streamlit/FastAPI
      (you already have the Streamlit muscle from [`image_processing_app/`](./image_processing_app))

**Practice:** Extend `image_processing_app` with a deep-learning-based feature
(e.g. add a classification or object-detection tab) instead of only classic CV ops.

**Estimated time:** 4–6 weeks+ (ongoing — this is where specialization deepens over time).

---

## Phase 7: Projects & Portfolio

- [ ] 1 classic CV project (e.g. document scanner, face blur tool)
- [ ] 1 CNN classification project on a real dataset (not MNIST/CIFAR — something you chose)
- [ ] 1 object detection or segmentation project
- [ ] 1 end-to-end deployed project (model + Streamlit/FastAPI + README write-up)
- [ ] Polish [README.md](./README.md) and each subfolder's docs as you complete phases

---

## How We'll Work Through This

- We alternate between tracks (e.g. OOP one session, DSA the next) so neither stalls.
- I'll explain concepts and give you problems to attempt first — not finished code.
- New code lands in the matching repo folder (`python/`, `DL/`, etc.) so this repo
  stays an honest record of the journey, not just a dump of answers.
- Come back to this file and check boxes off as phases complete — tell me to update it any time.

---

## Reference Resources

- **codebasics** — Python, DSA, and ML/DL YouTube playlists (primary roadmap source)
- **DSN Deeptech Cohort 3** — structured CV coursework, parallel track
- **Coursera: Mathematics for Machine Learning** — already completed, revisit Phase 4 topics as needed
- LeetCode / HackerRank — DSA practice
- PyTorch official tutorials — once Phase 5 begins
#TOMORROW BEGIN DSA AND PYTHON FOR DATA
