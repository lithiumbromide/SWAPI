---
title: "PatternId Property (IFaceHatch)"
project: "SOLIDWORKS API Help"
interface: "IFaceHatch"
member: "PatternId"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFaceHatch~PatternId.html"
---

# PatternId Property (IFaceHatch)

Gets the pattern ID of this face hatch. Read-only.

## Syntax

### Visual Basic (Declaration)

```vb
Property PatternId As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IFaceHatch
Dim value As System.Integer

instance.PatternId = value

value = instance.PatternId
```

### C#

```csharp
System.int PatternId {get; set;}
```

### C++/CLI

```cpp
property System.int PatternId {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Pattern IDs as found in <install_dir>\lang\<language>\SLDWRKS.PTN

## VBA Syntax

See [FaceHatch::PatternId](ms-its:sldworksapivb6.chm::/sldworks~FaceHatch~PatternId.html).

## See Also

[IFaceHatch Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFaceHatch.html)
[IFaceHatch Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFaceHatch_members.html)

## Availability

SOLIDWORKS 2004 FCS, Revision Number 12.0
