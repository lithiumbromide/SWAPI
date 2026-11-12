---
title: "AssemblyDoc::InsertCavity2"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/AssemblyDoc/AssemblyDoc__InsertCavity2.htm"
---

# AssemblyDoc::InsertCavity2

This method is obsolete and has been superseded by [AssemblyDoc::InsertCavity3](AssemblyDoc__InsertCavity3.htm).

Description

This method inserts a cavity to the active part using a selected component. This operation is performed in the context of an assembly document. The component being edited in the context of the assembly will receive the new Cavity feature.

Syntax (OLE Automation)

void AssemblyDoc.InsertCavity2 ( scaleFactor, scaleType)

| Input: | (double) scaleFactor | Scaling factor |
| --- | --- | --- |
| Input: | (long) scaleType | Type of scaling |

Syntax (COM)

status = AssemblyDoc->InsertCavity2 ( scaleFactor, scaleType )

| Input: | (double) scaleFactor | Scaling factor |
| --- | --- | --- |
| Input: | (long) scaleType | Type of scaling |
| Return: | (HRESULT)status | S_OK if successful |

Remarks

Set the scaleFactor parameter appropriately for your casting material. Express the scaling factor as a percent (+/- 20%) of the size of the cavity part, passing a value between -20 and +20.

The formula used to determine the size of the cavity is:

```vb
cavitysize = partsize * (1 + scaleFactor/100)
```

The scaleType parameter specifies the type of scaling. Options include:

| 0 | About component centroids |
| --- | --- |
| 1 | About component origins |
| 2 | About mold base origin |
