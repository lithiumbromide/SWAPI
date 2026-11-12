---
title: "InsertProtrusionSwept3 Method (IModelDoc)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc"
member: "InsertProtrusionSwept3"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc~InsertProtrusionSwept3.html"
---

# InsertProtrusionSwept3 Method (IModelDoc)

Obsolete. Superseded by [IModelDoc2::InsertProtrusionSwept3](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~InsertProtrusionSwept3.html).

## Syntax

### Visual Basic (Declaration)

```vb
Sub InsertProtrusionSwept3( _
   ByVal Propagate As System.Boolean, _
   ByVal Alignment As System.Boolean, _
   ByVal TwistCtrlOption As System.Short, _
   ByVal KeepTangency As System.Boolean, _
   ByVal ForceNonRational As System.Boolean, _
   ByVal StartMatchingType As System.Short, _
   ByVal EndMatchingType As System.Short _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc
Dim Propagate As System.Boolean
Dim Alignment As System.Boolean
Dim TwistCtrlOption As System.Short
Dim KeepTangency As System.Boolean
Dim ForceNonRational As System.Boolean
Dim StartMatchingType As System.Short
Dim EndMatchingType As System.Short

instance.InsertProtrusionSwept3(Propagate, Alignment, TwistCtrlOption, KeepTangency, ForceNonRational, StartMatchingType, EndMatchingType)
```

### C#

```csharp
void InsertProtrusionSwept3(
   System.bool Propagate,
   System.bool Alignment,
   System.short TwistCtrlOption,
   System.bool KeepTangency,
   System.bool ForceNonRational,
   System.short StartMatchingType,
   System.short EndMatchingType
)
```

### C++/CLI

```cpp
void InsertProtrusionSwept3(
   System.bool Propagate,
   System.bool Alignment,
   System.short TwistCtrlOption,
   System.bool KeepTangency,
   System.bool ForceNonRational,
   System.short StartMatchingType,
   System.short EndMatchingType
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Propagate`:
- `Alignment`:
- `TwistCtrlOption`:
- `KeepTangency`:
- `ForceNonRational`:
- `StartMatchingType`:
- `EndMatchingType`:

## VBA Syntax

See [ModelDoc::InsertProtrusionSwept3](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc~InsertProtrusionSwept3.html).

## See Also

[IModelDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc.html)
[IModelDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc_members.html)
