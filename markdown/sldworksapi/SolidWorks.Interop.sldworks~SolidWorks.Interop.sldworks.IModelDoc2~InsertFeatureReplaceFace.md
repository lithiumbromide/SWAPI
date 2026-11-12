---
title: "InsertFeatureReplaceFace Method (IModelDoc2)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc2"
member: "InsertFeatureReplaceFace"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~InsertFeatureReplaceFace.html"
---

# InsertFeatureReplaceFace Method (IModelDoc2)

Creates a Replace Face feature.

## Syntax

### Visual Basic (Declaration)

```vb
Sub InsertFeatureReplaceFace()
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc2

instance.InsertFeatureReplaceFace()
```

### C#

```csharp
void InsertFeatureReplaceFace()
```

### C++/CLI

```cpp
void InsertFeatureReplaceFace();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

True if the edges match, false if not

## VBA Syntax

See [ModelDoc2::InsertFeatureReplaceFace](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc2~InsertFeatureReplaceFace.html).

## Examples

[Create Replace Face Feature (VBA)](Replace_Face_Example_VB.htm)
[Create Replace Face Feature (VB.NET)](Replace_Face_Example_VBNET.htm)
[Create Replace Face Feature (C#)](Replace_Face_Example_CSharp.htm)

## Remarks

Before calling this method, select the faces to replace by calling [IModelDocExtension::SelectByID2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SelectByID2.html) with Marks of 1 and select the replacement surfaces by calling IModelDocExtension::SelectByID2 with Marks of 2.

See SOLIDWORKS Help for details about the Replace Face feature.

## See Also

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.html)
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.html)
[IReplaceFaceFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IReplaceFaceFeatureData.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
