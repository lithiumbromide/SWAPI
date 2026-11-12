---
title: "eDImageByRef Class"
project: ""
interface: "eDImageByRef"
member: ""
kind: "class"
source: "emodeltoolkit/eDImageByRef/eDImageByRef_Class.htm"
---

# eDImageByRef Class

| See Also | Example | Accessors | Availability |
| --- | --- | --- | --- |

Contains the dimensions of a bitmap and the bitmap data.

#### Header file code

```vb
class eDImageByRef : public eDImage
{
public:

eDImageByRef( int width = 0, int height = 0, const UCHAR *bits = NULL, eDImageType type = eDImageUnknown );

~eDImageByRef();

};
```
