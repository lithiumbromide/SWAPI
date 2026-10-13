---
title: "SelectionState Property (IIndentFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IIndentFeatureData"
member: "SelectionState"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IIndentFeatureData~SelectionState.html"
---

# SelectionState Property (IIndentFeatureData)

Gets or sets the side of the model to keep or remove.

## Syntax

### Visual Basic (Declaration)

```vb
Property SelectionState As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IIndentFeatureData
Dim value As System.Integer

instance.SelectionState = value

value = instance.SelectionState
```

### C#

```csharp
System.int SelectionState {get; set;}
```

### C++/CLI

```cpp
property System.int SelectionState {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Side of the model to keep or remove as defined in [swIndentSelectionState_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swIndentSelectionState_e.html)

## VBA Syntax

See [IndentFeatureData::SelectionState](ms-its:sldworksapivb6.chm::/sldworks~IndentFeatureData~SelectionState.html).

## Remarks

Setting this property inverts the side of the [target body](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IIndentFeatureData~TargetBody.html) to indent.

## See Also

[IIndentFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IIndentFeatureData.html)
[IIndentFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IIndentFeatureData_members.html)

## Availability

SOLIDWORKS 2016 FCS, Revision Number 24.0
