# Tree tournament skill assignment optimization

**Date:** 2026-03-27  
**Source:** Claude Web/App  
**ID:** `3000cf0d-300f-4658-99b2-732da1028854`

**Summary:** **Conversation Overview**

The person is working on a competitive programming problem involving a tournament tree structure. They shared existing C++ code that used a BFS-based approach with subtree sorting and asked Claude to implement a new methodology after the original was failing on late-stage test cases. The core problem involves assigning skill values to leaves of a tree to maximize total "happiness" (sum of skills of players in each match), where only the winner of each subtree advances to compete at the parent node.

Claude iteratively developed and refined a DFS-based solution across several attempts. The first approach computed leaf depths and used the rearrangement inequality, but this was logically incorrect because it assumed every player plays in all ancestor matches rather than only the winner advancing. Claude corrected this with a bottom-up DFS that increments only the top element (winner) of each child's count vector, then merges and sorts. This passed correctness but hit time limit exceeded (TLE) on the third test case. Claude then attempted optimizations using `inplace_merge`, then `multiset`, and finally settled on a `map<int,int>` frequency-map approach with small-to-large merging, which compresses duplicate count values to reduce merge cost.

The person has two explicit formatting preferences that were stated and must be maintained: no comments in the code, and every `for`, `if`, or other control flow statement must use curly braces even for single-line bodies. The final solution uses a recursive DFS returning `map<int,int>*` pointers, small-to-large merging of child maps, winner increment via map top-element manipulation, and a descending iteration over the merged frequency map to compute the answer by pairing sorted skills with sorted match counts.

---

## User

this is failing on late stage test case, implement the new methodology

```
#include <bits/stdc++.h>

// #define DEBUG

#ifdef DEBUG
std::ifstream fin("debugin.txt");
std::ofstream fout("debugout.txt");
#define cout fout  // writes all cout to file
#define cin fin    // reads all cin from file

#else

#endif

using namespace std;

template<typename A, typename B>
ostream& operator<<(ostream& os, const pair<A, B>& p) {
  return os << '(' << p.first << ", " << p.second << ')';
}
template<typename T_container,
         typename T = typename enable_if<!is_same<T_container, string>::value,
                                         typename T_container::value_type>::type>
ostream& operator<<(ostream& os, const T_container& v) {
  os << '{';
  string sep;
  for (const T& x : v)
    os << sep << x, sep = ", ";
  return os << '}';
}
void dbg_out() {
  cerr << endl;
}
template<typename Head, typename... Tail>
void dbg_out(Head H, Tail... T) {
  cerr << ' ' << H;
  dbg_out(T...);
}
#ifdef LOCAL
#define dbg(...) cerr << "(" << #VA_ARGS << "):", dbg_out(VA_ARGS)
#else
#define dbg(...)
#endif

#define ar array
#define ll long long
#define ld long double
#define sza(x) ((int)x.size())
#define all(a) (a).begin(), (a).end()

const int MAX_N = 1e5 + 5;
const ll MOD = 1e9 + 7;
const ll INF = 1e9;
const ld EPS = 1e-9;

vector<int> children[MAX_N];
int internal_count[MAX_N];

void dfs_internal(int u) {
  if (children[u].empty()) {
    internal_count[u] = 0;
    return;
  }
  internal_count[u] = 1;
  for (int v : children[u]) {
    dfs_internal(v);
    internal_count[u] += internal_count[v];
  }
}

void solve() {
  int N, K;
  cin >> N >> K;
  vector<ll> skills(K);
  for (int i = 0; i < K; i++) {
    cin >> skills[i];
  }
  sort(skills.rbegin(), skills.rend());

  for (int i = 1; i < N; i++) {
    int P;
    cin >> P;
    children[P].push_back(i);
  }

  dfs_internal(0);

  ll ans = 0;
  int idx = 0;
  queue<pair<int, ll>> q;
  q.push({0, skills[idx++]});

  while (!q.empty()) {
    auto [u, w] = q.front();
    q.pop();
    if (children[u].empty()) {
      continue;
    }

    vector<int> sorted_children = children[u];
    sort(sorted_children.begin(), sorted_children.end(),
         [](int a, int b) { return internal_count[a] > internal_count[b]; });

    int m = sorted_children.size();
    ll match_total = w;
    vector<ll> child_winners(m);
    child_winners[0] = w;
    for (int i = 1; i < m; i++) {
      child_winners[i] = skills[idx++];
      match_total += child_winners[i];
    }
    ans += match_total;

    for (int i = 0; i < m; i++) {
      q.push({sorted_children[i], child_winners[i]});
    }
  }

  cout << ans << '\n';
}

int main() {
  ios_base::sync_with_stdio(0);
  cin.tie(0);
  cout.tie(0);
  int tc = 1;
  // cin >> tc;
  for (int t = 1; t <= tc; t++) {
    // cout << "Case #" << t << ": ";
    solve();
  }
}

```



smart dfs, consider local children in the dfs.

> **File:** 1774572196940_image.png

> **File:** 1774572203996_image.png

---

## Assistant

Looking at this problem, the key insight is: each player's skill value contributes to the total happiness once for every match they participate in. The most skilled player wins every match they're in, so we want to maximize how many matches the top players play in.

**Core observation:** A player assigned to a subtree will participate in exactly (number of internal nodes on their path from leaf to root within that subtree) matches. So we want to assign higher skill values to leaves that have more ancestors (deeper internal node paths).

The current BFS approach greedily sorts children by subtree size, but the assignment within the BFS ordering doesn't correctly reflect the actual "number of matches a player participates in" for each leaf position.

**New methodology:** DFS where we compute for each leaf its "depth in terms of internal nodes" (i.e., how many internal nodes are on the path from root to that leaf, inclusive). Sort all leaves by this count descending, assign top skills to highest-count leaves, then answer = sum over all leaves of skill[leaf] × internal_node_depth[leaf].

Here's the corrected solution:

```cpp
#include <bits/stdc++.h>
using namespace std;

#define ll long long
const int MAX_N = 1e5 + 5;
vector<int> children[MAX_N];

// For each leaf, count how many internal nodes are on path from root to leaf (inclusive)
// An internal node is one with children
void dfs(int u, int depth, vector<int>& leaf_depths) {
    if (children[u].empty()) {
        // u is a leaf, depth = number of internal nodes above it (root counts if it has children)
        leaf_depths.push_back(depth);
        return;
    }
    for (int v : children[u]) {
        dfs(v, depth + 1, leaf_depths);
    }
}

void solve() {
    int N, K;
    cin >> N >> K;
    vector<ll> skills(K);
    for (int i = 0; i < K; i++) cin >> skills[i];
    sort(skills.rbegin(), skills.rend());

    for (int i = 1; i < N; i++) {
        int P;
        cin >> P;
        children[P].push_back(i);
    }

    vector<int> leaf_depths;
    dfs(0, 1, leaf_depths); // root is internal (guaranteed K leaves, N >= 3)

    // Sort leaf depths descending — assign best players to most-matched positions
    sort(leaf_depths.rbegin(), leaf_depths.rend());

    ll ans = 0;
    for (int i = 0; i < K; i++) {
        ans += skills[i] * (ll)leaf_depths[i];
    }

    cout << ans << '\n';
}

int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    solve();
}
```

**Why this works:**

- Each match at an internal node contributes the sum of skills of all players whose path passes through it
- Equivalently, each player contributes their skill × (number of internal nodes on their root-to-leaf path)
- So total happiness = Σ skill[i] × depth[leaf_i], where depth counts internal nodes
- To maximize: sort skills descending, sort depths descending, pair greedily (rearrangement inequality)

**Verify with Sample 1:** Tree has 5 nodes, 3 leaves. Skills = [5,4,3]. The tree structure gives leaf depths — the answer should be 17. With depths like [2,2,1]: 5×2 + 4×2 + 3×1 = 10+8+3 = 21 ≠ 17... let me re-check the sample tree.

For sample 1: nodes 0-4, parents: node1→0, node2→0, node3→1, node4→1. So node 0 has children {1,2}, node 1 has children {3,4}, leaves are {2,3,4}. Depths (internal nodes on path): leaf 2 has path 0→2, depth=1. Leaf 3: 0→1→3, depth=2. Leaf 4: 0→1→4, depth=2. Depths=[2,2,1], skills=[5,4,3]: 5×2+4×2+3×1 = 10+8+3 = **21**, but expected is **17**.

There's a subtlety — the winner of each match "carries" their skill, so the top player doesn't add their skill at every level independently. Let me reconsider... actually the happiness at a node is the **sum of skills of all players in that match**, and the winner carries forward. So each player contributes their skill for every match they **personally play**, which equals their internal-node-depth. 5×2+4×2+3×1=21≠17.

Hmm, re-reading: at each internal node with m children, there are m players competing (the winners from each child subtree), producing **one match** with happiness = sum of those m skills. So each player's contribution = number of internal node ancestors (not the node itself that sends them up). Let me recount: leaf 3's path internal nodes above it = just node 0 and node 1 = 2 matches it participates in. That gives 21 still.

Wait — at node 1, players from leaves 3 and 4 meet: happiness = skill[3]+skill[4]. Winner goes to node 0 and meets skill[2]: happiness += skill[winner]+skill[2]. So player at leaf 3 participates in 2 matches only if they win at node 1. **The winner always wins**, so top player plays in ALL internal nodes on their path. So depth is correct. But 21≠17...

Let me re-examine: skills sorted = [5,4,3]. Optimal assignment: put 5 at leaf 3 or 4 (depth 2). Put 4 at the other depth-2 leaf. Put 3 at leaf 2 (depth 1). Match at node1: 5+4=9. Match at node0: 5+3=8. Total=17. ✓

The issue: **player skill contributes only when THEY play**, and the loser doesn't continue. So player with skill 4 only plays 1 match (at node 1, loses to 5). Their contribution is 4×1, not 4×2!

So the correct model: **each player's contribution = number of matches they personally play = number of internal nodes from their starting leaf up to where they lose** (or all the way if they're the champion). The winner plays depth matches, but others play fewer.

This is a more complex DP problem. The correct approach:

```cpp
#include <bits/stdc++.h>
using namespace std;
#define ll long long
const int MAX_N = 1e5 + 5;
vector<int> children[MAX_N];

// Returns sorted list of "match counts" for each leaf position in this subtree
// match_counts[i] = number of matches the i-th best player assigned here will play
// We return them sorted descending so we can greedily assign
vector<int> dfs(int u) {
    if (children[u].empty()) {
        return {0}; // leaf plays 0 matches initially; gets +1 from parent
    }
    
    // Gather match count vectors from all children
    vector<vector<int>> child_vecs;
    for (int v : children[u]) {
        child_vecs.push_back(dfs(v));
    }
    
    // Each child sends its best player (winner) to compete at this node
    // All players in each child subtree get +1 match (for the match at this node... 
    // wait, only the winner of each subtree plays at this node)
    
    // At node u with m children: m players meet (one winner per child subtree)
    // The overall best player wins all m-1 matches here... no, it's ONE match with m players
    // Actually re-reading: "whenever any number of players play a game" -> one match per internal node
    // So at node u: exactly 1 match, involving m players (winners from each child)
    // The single best among them wins and proceeds up
    
    // For each child subtree, the winner of that subtree plays 1 match at node u
    // So every leaf's contribution gets +1 only if they are the winner of their subtree path up to u
    
    // This means: for child subtree i, only the TOP player (their winner) gets +1 from this node
    // We want to maximize total, so we merge all child winner lists and assign optimally
    
    // Key insight for merging: 
    // From child i's perspective, their best player wins all matches in child i's subtree
    // AND plays 1 more match at node u (wins or loses)
    // The overall best player among all children wins at u and proceeds further up
    
    // When merging m children at node u:
    // - Take the best player overall: they get +1 (play at u) + whatever they got in their subtree
    // - For all other children's best players: they get +1 (play at u, then lose)
    // - Everyone else: no change
    
    // So the merged sorted match-count list:
    // Sort all child "winner counts" (first element of each child vec) — assign best skill to highest
    // The non-winners within each subtree just keep their counts
    
    // Let's think of it as: collect all leaf positions across all children
    // Each leaf position has a "base count" from its subtree
    // Additionally, the winner of each child subtree gets +1 from the match at u
    // The winner among those winners gets further +1s from ancestors
    // But we're computing bottom-up, so here we just add +1 to each child's top player
    
    // Merge: increment top of each child vector by 1, then merge-sort all
    vector<int> merged;
    for (auto& cv : child_vecs) {
        cv[0] += 1; // winner of this subtree plays at node u
        for (int x : cv) merged.push_back(x);
    }
    sort(merged.rbegin(), merged.rend());
    return merged;
}

void solve() {
    int N, K;
    cin >> N >> K;
    vector<ll> skills(K);
    for (int i = 0; i < K; i++) cin >> skills[i];
    sort(skills.rbegin(), skills.rend());

    for (int i = 1; i < N; i++) {
        int P; cin >> P;
        children[P].push_back(i);
    }

    vector<int> counts = dfs(0);
    // counts[i] = matches played by i-th best player
    
    ll ans = 0;
    for (int i = 0; i < K; i++) {
        ans += skills[i] * (ll)counts[i];
    }
    cout << ans << '\n';
}

int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    solve();
}
```

Let me verify sample 1: Leaves 2,3,4. 
- `dfs(3)` = [0], `dfs(4)` = [0]  
- `dfs(1)`: children are 3,4. Each winner gets +1: [1],[1]. Merged sorted: [1,1]
- `dfs(2)` = [0]
- `dfs(0)`: children are 1,2. From child 1: top gets +1 → [2,1]. From child 2: top gets +1 → [1]. Merged: [2,1,1]

Answer: 5×2 + 4×1 + 3×1 = 10+4+3 = **17** ✓

Verify sample 2 would need tracing through the larger tree but the logic holds. However this DFS returns and sorts vectors which could be O(K log K) per node — potentially O(NK log K) total which may be too slow for N=10^5.

**Optimized version** using the "small-to-large" / sorted-merge insight — but first let's check if the naive version passes, then optimize if needed:

```cpp
#include <bits/stdc++.h>
using namespace std;
#define ll long long
const int MAX_N = 1e5 + 5;
vector<int> children[MAX_N];

vector<int> dfs(int u) {
    if (children[u].empty()) return {0};
    
    vector<vector<int>> child_vecs;
    for (int v : children[u]) {
        child_vecs.push_back(dfs(v));
    }
    
    vector<int> merged;
    for (auto& cv : child_vecs) {
        cv[0]++;
        for (int x : cv) merged.push_back(x);
    }
    sort(merged.rbegin(), merged.rend());
    return merged;
}

void solve() {
    int N, K;
    cin >> N >> K;
    vector<ll> skills(K);
    for (int i = 0; i < K; i++) cin >> skills[i];
    sort(skills.rbegin(), skills.rend());

    for (int i = 1; i < N; i++) {
        int P; cin >> P;
        children[P].push_back(i);
    }

    vector<int> counts = dfs(0);
    
    ll ans = 0;
    for (int i = 0; i < K; i++) ans += skills[i] * (ll)counts[i];
    cout << ans << '\n';
}

int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    solve();
}
```

The sorting at each internal node is the bottleneck. In the worst case (a balanced binary tree with K=N/2 leaves), total work is O(K log²K) via merge-sort tree arguments — this should be acceptable for K≤10^5. The key correctness fix from your original is: **only the winner of each child subtree gets +1 for the match at the parent node, not all players in the subtree.**

---

## User

give with no comments

---

## Assistant

```cpp
#include <bits/stdc++.h>
using namespace std;
#define ll long long
const int MAX_N = 1e5 + 5;
vector<int> children[MAX_N];

vector<int> dfs(int u) {
    if (children[u].empty()) return {0};
    
    vector<vector<int>> child_vecs;
    for (int v : children[u]) {
        child_vecs.push_back(dfs(v));
    }
    
    vector<int> merged;
    for (auto& cv : child_vecs) {
        cv[0]++;
        for (int x : cv) merged.push_back(x);
    }
    sort(merged.rbegin(), merged.rend());
    return merged;
}

void solve() {
    int N, K;
    cin >> N >> K;
    vector<ll> skills(K);
    for (int i = 0; i < K; i++) cin >> skills[i];
    sort(skills.rbegin(), skills.rend());

    for (int i = 1; i < N; i++) {
        int P; cin >> P;
        children[P].push_back(i);
    }

    vector<int> counts = dfs(0);
    
    ll ans = 0;
    for (int i = 0; i < K; i++) ans += skills[i] * (ll)counts[i];
    cout << ans << '\n';
}

int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    solve();
}
```

---

## User

getting time limit exceeded 3rd test case

---

## Assistant

The merge+sort at each node is too slow. Use priority-queue merge (small-to-large style) — merge all children's sorted structures efficiently:

```cpp
#include <bits/stdc++.h>
using namespace std;
#define ll long long
const int MAX_N = 1e5 + 5;
vector<int> children[MAX_N];

vector<int>* dfs(int u) {
    if (children[u].empty()) {
        return new vector<int>{0};
    }

    vector<vector<int>*> child_vecs;
    for (int v : children[u]) {
        child_vecs.push_back(dfs(v));
    }

    // increment top of each child (winner gets +1)
    for (auto* cv : child_vecs) {
        (*cv)[0]++;
    }

    // small-to-large merge: always merge smaller into larger
    sort(child_vecs.begin(), child_vecs.end(), [](vector<int>* a, vector<int>* b) {
        return a->size() > b->size();
    });

    vector<int>* base = child_vecs[0];
    for (int i = 1; i < (int)child_vecs.size(); i++) {
        for (int x : *child_vecs[i]) base->push_back(x);
        delete child_vecs[i];
    }

    sort(base->rbegin(), base->rend());
    return base;
}

void solve() {
    int N, K;
    cin >> N >> K;
    vector<ll> skills(K);
    for (int i = 0; i < K; i++) cin >> skills[i];
    sort(skills.rbegin(), skills.rend());

    for (int i = 1; i < N; i++) {
        int P; cin >> P;
        children[P].push_back(i);
    }

    vector<int>* counts = dfs(0);

    ll ans = 0;
    for (int i = 0; i < K; i++) ans += skills[i] * (ll)(*counts)[i];
    cout << ans << '\n';
    delete counts;
}

int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    solve();
}
```

The small-to-large merge keeps total insertions at O(K log K), and the final sort at each node operates on already-nearly-sorted data. But the sort is still called at every internal node on the full merged vector.

A cleaner O(K log² K) approach — use a `multiset` or merge with `std::inplace_merge`:

```cpp
#include <bits/stdc++.h>
using namespace std;
#define ll long long
const int MAX_N = 1e5 + 5;
vector<int> children[MAX_N];

vector<int>* dfs(int u) {
    if (children[u].empty()) {
        return new vector<int>{0};
    }

    vector<vector<int>*> child_vecs;
    for (int v : children[u]) {
        child_vecs.push_back(dfs(v));
    }

    for (auto* cv : child_vecs) {
        (*cv)[0]++;
        sort(cv->begin(), cv->end(), greater<int>());
    }

    sort(child_vecs.begin(), child_vecs.end(), [](vector<int>* a, vector<int>* b) {
        return a->size() > b->size();
    });

    vector<int>* base = child_vecs[0];
    for (int i = 1; i < (int)child_vecs.size(); i++) {
        size_t old_size = base->size();
        for (int x : *child_vecs[i]) base->push_back(x);
        inplace_merge(base->begin(), base->begin() + old_size, base->end(), greater<int>());
        delete child_vecs[i];
    }

    return base;
}

void solve() {
    int N, K;
    cin >> N >> K;
    vector<ll> skills(K);
    for (int i = 0; i < K; i++) cin >> skills[i];
    sort(skills.rbegin(), skills.rend());

    for (int i = 1; i < N; i++) {
        int P; cin >> P;
        children[P].push_back(i);
    }

    vector<int>* counts = dfs(0);

    ll ans = 0;
    for (int i = 0; i < K; i++) ans += skills[i] * (ll)(*counts)[i];
    cout << ans << '\n';
    delete counts;
}

int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    solve();
}
```

`inplace_merge` on two already-sorted halves is O(n) with buffer or O(n log n) worst case, but avoids re-sorting the entire vector each time. Combined with small-to-large ordering of children this should comfortably handle K=10^5.

---

## User

ensure each for loop or if statement or other loops have brackets even if its a one liner

---

## Assistant

```cpp
#include <bits/stdc++.h>
using namespace std;
#define ll long long
const int MAX_N = 1e5 + 5;
vector<int> children[MAX_N];

vector<int>* dfs(int u) {
    if (children[u].empty()) {
        return new vector<int>{0};
    }

    vector<vector<int>*> child_vecs;
    for (int v : children[u]) {
        child_vecs.push_back(dfs(v));
    }

    for (auto* cv : child_vecs) {
        (*cv)[0]++;
        sort(cv->begin(), cv->end(), greater<int>());
    }

    sort(child_vecs.begin(), child_vecs.end(), [](vector<int>* a, vector<int>* b) {
        return a->size() > b->size();
    });

    vector<int>* base = child_vecs[0];
    for (int i = 1; i < (int)child_vecs.size(); i++) {
        size_t old_size = base->size();
        for (int x : *child_vecs[i]) {
            base->push_back(x);
        }
        inplace_merge(base->begin(), base->begin() + old_size, base->end(), greater<int>());
        delete child_vecs[i];
    }

    return base;
}

void solve() {
    int N, K;
    cin >> N >> K;
    vector<ll> skills(K);
    for (int i = 0; i < K; i++) {
        cin >> skills[i];
    }
    sort(skills.rbegin(), skills.rend());

    for (int i = 1; i < N; i++) {
        int P;
        cin >> P;
        children[P].push_back(i);
    }

    vector<int>* counts = dfs(0);

    ll ans = 0;
    for (int i = 0; i < K; i++) {
        ans += skills[i] * (ll)(*counts)[i];
    }
    cout << ans << '\n';
    delete counts;
}

int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    solve();
}
```

---

## User

still getting tle

---

## Assistant

Let me think about this more carefully. The counts vector only needs the sorted match-counts, and the key observation is: **the counts vector values are bounded by tree depth, not K**. Let me use a frequency/bucket approach and think about what values actually appear.

Actually the real fix is: instead of storing and sorting all K values, compute the answer directly during DFS using a **priority-queue merge** so we never re-sort large arrays:

```cpp
#include <bits/stdc++.h>
using namespace std;
#define ll long long
const int MAX_N = 1e5 + 5;
vector<int> children[MAX_N];

// Returns sorted (descending) match counts for all leaves in subtree
// Using DSU on tree / small-to-large with sorted multisets
multiset<int, greater<int>>* dfs(int u) {
    if (children[u].empty()) {
        auto* s = new multiset<int, greater<int>>();
        s->insert(0);
        return s;
    }

    vector<multiset<int, greater<int>>*> child_sets;
    for (int v : children[u]) {
        child_sets.push_back(dfs(v));
    }

    // increment max element of each child set (winner gets +1)
    for (auto* cs : child_sets) {
        auto it = cs->begin();
        int val = *it;
        cs->erase(it);
        cs->insert(val + 1);
    }

    // small-to-large: merge all into largest
    sort(child_sets.begin(), child_sets.end(), [](auto* a, auto* b) {
        return a->size() > b->size();
    });

    multiset<int, greater<int>>* base = child_sets[0];
    for (int i = 1; i < (int)child_sets.size(); i++) {
        for (int x : *child_sets[i]) {
            base->insert(x);
        }
        delete child_sets[i];
    }

    return base;
}

void solve() {
    int N, K;
    cin >> N >> K;
    vector<ll> skills(K);
    for (int i = 0; i < K; i++) {
        cin >> skills[i];
    }
    sort(skills.rbegin(), skills.rend());

    for (int i = 1; i < N; i++) {
        int P;
        cin >> P;
        children[P].push_back(i);
    }

    multiset<int, greater<int>>* counts = dfs(0);

    ll ans = 0;
    int i = 0;
    for (int c : *counts) {
        ans += skills[i++] * (ll)c;
    }
    cout << ans << '\n';
    delete counts;
}

int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    solve();
}
```

But multiset insert is O(log K) per element, total O(K log²K) with small-to-large. If still TLE, the ultimate fix is to avoid storing counts at all and instead track **how many leaves have each count** using a map, merged small-to-large:

```cpp
#include <bits/stdc++.h>
using namespace std;
#define ll long long
const int MAX_N = 1e5 + 5;
vector<int> children[MAX_N];

// map: match_count -> frequency
map<int, int>* dfs(int u) {
    if (children[u].empty()) {
        auto* m = new map<int, int>();
        (*m)[0] = 1;
        return m;
    }

    vector<map<int, int>*> child_maps;
    for (int v : children[u]) {
        child_maps.push_back(dfs(v));
    }

    // increment the top count entry by 1 for each child's winner
    for (auto* cm : child_maps) {
        auto it = cm->end();
        --it;
        int top_val = it->first;
        int top_cnt = it->second;
        cm->erase(it);
        if (top_cnt > 1) {
            (*cm)[top_val] = top_cnt - 1;
        }
        (*cm)[top_val + 1]++;
    }

    // small-to-large merge
    sort(child_maps.begin(), child_maps.end(), [](auto* a, auto* b) {
        return a->size() > b->size();
    });

    map<int, int>* base = child_maps[0];
    for (int i = 1; i < (int)child_maps.size(); i++) {
        for (auto& [val, freq] : *child_maps[i]) {
            (*base)[val] += freq;
        }
        delete child_maps[i];
    }

    return base;
}

void solve() {
    int N, K;
    cin >> N >> K;
    vector<ll> skills(K);
    for (int i = 0; i < K; i++) {
        cin >> skills[i];
    }
    sort(skills.rbegin(), skills.rend());

    for (int i = 1; i < N; i++) {
        int P;
        cin >> P;
        children[P].push_back(i);
    }

    map<int, int>* counts = dfs(0);

    // iterate descending by count, assign best skills first
    ll ans = 0;
    int idx = 0;
    for (auto it = counts->rbegin(); it != counts->rend(); ++it) {
        int match_count = it->first;
        int freq = it->second;
        for (int j = 0; j < freq; j++) {
            ans += skills[idx++] * (ll)match_count;
        }
    }
    cout << ans << '\n';
    delete counts;
}

int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    solve();
}
```

The map approach compresses duplicate count values so the map size is bounded by the number of **distinct depth values** (at most O(log K) for balanced trees, O(depth) worst case) rather than K, making small-to-large merges much cheaper. This should resolve TLE.

---

## User

no comments, and ensure statement bracket rule still applies

---

## Assistant

```cpp
#include <bits/stdc++.h>
using namespace std;
#define ll long long
const int MAX_N = 1e5 + 5;
vector<int> children[MAX_N];

map<int, int>* dfs(int u) {
    if (children[u].empty()) {
        auto* m = new map<int, int>();
        (*m)[0] = 1;
        return m;
    }

    vector<map<int, int>*> child_maps;
    for (int v : children[u]) {
        child_maps.push_back(dfs(v));
    }

    for (auto* cm : child_maps) {
        auto it = cm->end();
        --it;
        int top_val = it->first;
        int top_cnt = it->second;
        cm->erase(it);
        if (top_cnt > 1) {
            (*cm)[top_val] = top_cnt - 1;
        }
        (*cm)[top_val + 1]++;
    }

    sort(child_maps.begin(), child_maps.end(), [](auto* a, auto* b) {
        return a->size() > b->size();
    });

    map<int, int>* base = child_maps[0];
    for (int i = 1; i < (int)child_maps.size(); i++) {
        for (auto& [val, freq] : *child_maps[i]) {
            (*base)[val] += freq;
        }
        delete child_maps[i];
    }

    return base;
}

void solve() {
    int N, K;
    cin >> N >> K;
    vector<ll> skills(K);
    for (int i = 0; i < K; i++) {
        cin >> skills[i];
    }
    sort(skills.rbegin(), skills.rend());

    for (int i = 1; i < N; i++) {
        int P;
        cin >> P;
        children[P].push_back(i);
    }

    map<int, int>* counts = dfs(0);

    ll ans = 0;
    int idx = 0;
    for (auto it = counts->rbegin(); it != counts->rend(); ++it) {
        int match_count = it->first;
        int freq = it->second;
        for (int j = 0; j < freq; j++) {
            ans += skills[idx++] * (ll)match_count;
        }
    }
    cout << ans << '\n';
    delete counts;
}

int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    solve();
}
```

---
