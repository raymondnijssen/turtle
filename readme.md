```mermaid
  flowchart TD;
      A[Deploy production] --> B{Is it Friday?};
      B -- Yes --> C[Do not deploy];
      B -- No --> D[Deploy];
      C --> E[Weekend!];
      D --> E[Weekend!];
```
