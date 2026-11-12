---
title: "GetBlockingState Method (IModelDoc2)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc2"
member: "GetBlockingState"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~GetBlockingState.html"
---

# GetBlockingState Method (IModelDoc2)

Gets the current value of the SOLIDWORKS blocking state, within the range of values accessible by [IModelDoc2::SetBlockingState](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~SetBlockingState.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function GetBlockingState() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc2
Dim value As System.Integer

value = instance.GetBlockingState()
```

### C#

```csharp
System.int GetBlockingState()
```

### C++/CLI

```cpp
System.int GetBlockingState();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

State as defined by [swBlockingStates_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swBlockingStates_e.html)

## VBA Syntax

See [ModelDoc2::GetBlockingState](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc2~GetBlockingState.html).

## Examples

[Get Blocking State (VBA)](Get_Blocking_State_Example_VB.htm)
[Set Blocking State (VBA)](Set_Blocking_State_Example_VB.htm)

## See Also

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.html)
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.html)
[IModelDoc2::ResetBlockingState Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ResetBlockingState.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
