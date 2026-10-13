---
title: "ResetBlockingState Method (IModelDoc2)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc2"
member: "ResetBlockingState"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ResetBlockingState.html"
---

# ResetBlockingState Method (IModelDoc2)

Resets the blocking state for the SOLIDWORKS menus.

## Syntax

### Visual Basic (Declaration)

```vb
Sub ResetBlockingState()
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc2

instance.ResetBlockingState()
```

### C#

```csharp
void ResetBlockingState()
```

### C++/CLI

```cpp
void ResetBlockingState();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

## VBA Syntax

See [ModelDoc2::ResetBlockingState](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc2~ResetBlockingState.html).

## Examples

[Set Blocking State (VBA)](Set_Blocking_State_Example_VB.htm)

## Remarks

Call this method after calling [IModelDoc2::SetBlockingState](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~SetBlockingState.html) to set the SOLIDWORKS menus back to their previous state.

NOTE: You must call this method every time you call IModelDoc2::SetBlockingState. It is not enough to call this method once at the end of a sequence of operations that have called IModelDoc2::SetBlockingState several times.

## See Also

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.html)
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
