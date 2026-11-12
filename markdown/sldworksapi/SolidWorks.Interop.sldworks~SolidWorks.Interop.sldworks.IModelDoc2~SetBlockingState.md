---
title: "SetBlockingState Method (IModelDoc2)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc2"
member: "SetBlockingState"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~SetBlockingState.html"
---

# SetBlockingState Method (IModelDoc2)

Sets the blocking state for the SOLIDWORKS menus.

## Syntax

### Visual Basic (Declaration)

```vb
Sub SetBlockingState( _
   ByVal StateIn As System.Integer _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc2
Dim StateIn As System.Integer

instance.SetBlockingState(StateIn)
```

### C#

```csharp
void SetBlockingState(
   System.int StateIn
)
```

### C++/CLI

```cpp
void SetBlockingState(
   System.int StateIn
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `StateIn`: State as defined in [swBlockingStates_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swBlockingStates_e.html)

## VBA Syntax

See [ModelDoc2::SetBlockingState](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc2~SetBlockingState.html).

## Examples

[Set Blocking State (VBA)](Set_Blocking_State_Example_VB.htm)

## Remarks

Call [IModelDoc2::ResetBlockingState](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~ResetBlockingState.html) to reset the state when the operations are completed.

IMPORTANT: There must be a corresponding call to IModelDoc2::ResetBlockingState for every call to IModelDoc2::SetBlockingState. It is not enough to call IModelDoc2::ResetBlockingState once at the end of a sequence of operations that have called IModelDoc2::SetBlockingState several times.

## See Also

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.html)
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.html)
[IModelDoc2::GetBlockingState Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~GetBlockingState.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
