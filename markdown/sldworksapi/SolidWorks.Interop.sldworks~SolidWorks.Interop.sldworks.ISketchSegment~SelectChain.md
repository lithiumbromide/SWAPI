---
title: "SelectChain Method (ISketchSegment)"
project: "SOLIDWORKS API Help"
interface: "ISketchSegment"
member: "SelectChain"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSegment~SelectChain.html"
---

# SelectChain Method (ISketchSegment)

Selects chains of entities attached to this sketch segment.

## Syntax

### Visual Basic (Declaration)

```vb
Function SelectChain( _
   ByVal Append As System.Boolean, _
   ByVal Data As SelectData _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISketchSegment
Dim Append As System.Boolean
Dim Data As SelectData
Dim value As System.Boolean

value = instance.SelectChain(Append, Data)
```

### C#

```csharp
System.bool SelectChain(
   System.bool Append,
   SelectData Data
)
```

### C++/CLI

```cpp
System.bool SelectChain(
   System.bool Append,
   SelectData^ Data
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Append`: True to append to the current selection list, false to replace the selection list
- `Data`: [ISelectData](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISelectData.html)

### Return Value

True if successful, false if not

## VBA Syntax

See [SketchSegment::SelectChain](ms-its:sldworksapivb6.chm::/sldworks~SketchSegment~SelectChain.html).

## Examples

[Select Chains of Entities Attached to a Sketch Segment (VBA)](Select_Chain_of_Entities_Example_VB.htm)
[Select Chains of Entities Attached to a Sketch Segment (VB.NET)](Select_Chain_of_Entities_Example_VBNET.htm)
[Select Chains of Entities Attached to a Sketch Segment (C#)](Select_Chain_of_Entities_Example_CSharp.htm)

## Remarks

Before calling this method call [ISelectionMgr::CreateSelectData](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISelectionMgr~CreateSelectData.html) to specify Data.

This method is equivalent to right-clicking a sketch segment and selecting **Select Chain**. The chain of entities in each direction is selected. Selection ends when a branch in the chain is encountered.

## See Also

[ISketchSegment Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSegment.html)
[ISketchSegment Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSegment_members.html)

## Availability

SOLIDWORKS 2012 FCS, Revision Number 20.0
