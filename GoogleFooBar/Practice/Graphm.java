class Graphm implements Graph {
    private int[][] matrix;                // The edge matrix
    private int numEdge;                   // Number of edges
    public int[] Mark;                     // The mark array
    
    public Graphm() {}                     // Constructors
    public Graphm(int n) {
      Init(n);
    }
    
    public void Init(int n) {
      Mark = new int[n];
      matrix = new int[n][n];
      numEdge = 0;
    }
    
    public int n() { return Mark.length; } // # of vertices
    public int e() { return numEdge; }     // # of edges
    
    /** @return v's first neighbor */
    public int first(int v) {
      for (int i=0; i<Mark.length; i++)
        if (matrix[v][i] != 0) return i;
      return Mark.length;  // No edge for this vertex
    }
    
    /** @return v's next neighbor after w */
    public int next(int v, int w) {
      for (int i=w+1; i<Mark.length; i++)
        if (matrix[v][i] != 0)
        return i;
      return Mark.length;  // No next edge;
    }
    
    /** Set the weight for an edge */
    public void setEdge(int i, int j, int wt) {
      assert wt!=0 : "Cannot set weight to 0";
      if (matrix[i][j] == 0) numEdge++;
      matrix[i][j] = wt;
    }
    
    /** Delete an edge */
    public void delEdge(int i, int j) { // Delete edge (i, j)
      if (matrix[i][j] != 0) numEdge--;
      matrix[i][j] = 0;
    }
    
    /** Determine if an edge is in the graph */
    public boolean isEdge(int i, int j)
    { return matrix[i][j] != 0; }
    
    /** @return an edge's weight */
    public int weight(int i, int j) {
      return matrix[i][j];
    }
    
    /** Set/Get the mark value for a vertex */
    public void setMark(int v, int val) { Mark[v] = val; }
    public int getMark(int v) { return Mark[v]; }
    
    
    // print out graph adjacency matrix
    public void printGraph(){
      for(int i=0; i<this.n(); i++){
        System.out.print(i+" : ");
        for(int j=0; j<this.n(); j++){
          System.out.print(matrix[i][j]+" ");
        }
        System.out.print("\n");
      }
    }
    
    // print out which vertices have been visited
    public void printVisited(){
      System.out.print("visited : ");
      for(int i=0; i<this.n(); i++){
        System.out.print(this.Mark[i]+" ");
      }
      System.out.print("\n");
    }
    
    /** Depth first search */
    public static void DFS(Graph G, int v) {
      preVisit(G, v); // Take appropriate action
      G.setMark(v, 1);
      for (int w = G.first(v); w < G.n() ; w = G.next(v, w)){
        if(G.getMark(w) == 0){
          DFS(G, w);
        }
      }
      postVisit(G, v); // Take appropriate action
    }
    
    // // breadth first search
    // public static void BFS(Graph G, int start) {
    //   Queue<Integer> Q = new AQueue<Integer>(G.n());
    //   Q.enqueue(start);
    //   G.setMark(start, 1);
    //   while (Q.length() > 0) { 
    //     int v = Q.dequeue();
    //     preVisit(G, v); 
    //     for (int w = G.first(v); w < G.n(); w = G.next(v, w))
    //       if (G.getMark(w) == 0) { 
    //       G.setMark(w, 1);
    //       Q.enqueue(w);
    //     } 
    //     postVisit(G, v); 
    //   }
    // }
    
    // pre-visit action
    public static void preVisit(Graph g, int v){
      System.out.println("Vertex "+v+" has been pre-visited.");
    }
    
    // post-visit action
    public static void postVisit(Graph g, int v){
      System.out.println("Vertex "+v+" has been post-visited.");
    }
    
    
    
    // prim's algorithm for MST
    public static void Prim(Graph G, int s, int[] D, int[] V) {
      for (int i=0; i<G.n(); i++)   
        D[i] = Integer.MAX_VALUE;
      D[s] = 0;
      for (int i=0; i<G.n(); i++) { 
        int v = minVertex(G, D);
        G.setMark(v, 1);
        if (v != s) AddEdgetoMST(V[v], v);
        if (D[v] == Integer.MAX_VALUE) return; 
        for (int w = G.first(v); w < G.n(); w = G.next(v, w))
          if (D[w] > G.weight(v, w) && G.getMark(w) == 0) {
          D[w] = G.weight(v, w);
          V[w] = v;
        }
      }
    }
    
    
    // method to add edges to the MST
    public static void AddEdgetoMST(int v1, int v2) {
      System.out.println("edge : "+v1+" - "+v2);
    }
    
    // method for the min value of unvisited vertices
    public static int minVertex(Graph G, int[] D) {
      int v = 0;  
      for (int i=0; i<G.n(); i++)
        if (G.getMark(i) == 0) { v = i; break; }
      for (int i=0; i<G.n(); i++)  
        if ((G.getMark(i) == 0) && (D[i] < D[v])){v = i;}
      return v;
    }
    
    
    
  }