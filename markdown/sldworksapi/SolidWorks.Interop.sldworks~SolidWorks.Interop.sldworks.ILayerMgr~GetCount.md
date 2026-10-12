---
title: "GetCount Method (ILayerMgr)"
project: "SOLIDWORKS API Help"
interface: "ILayerMgr"
member: "GetCount"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILayerMgr~GetCount.html"
---

# GetCount Method (ILayerMgr)

Gets the number of layers in this drawing document.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetCount() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ILayerMgr
Dim value As System.Integer

value = instance.GetCount()
```

### C#

```csharp
System.int GetCount()
```

### C++/CLI

```cpp
System.int GetCount();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Number of layers

## VBA Syntax

See [LayerMgr::GetCount](ms-its:sldworksapivb6.chm::/sldworks~LayerMgr~GetCount.html).

## Remarks

Call this method before calling [ILayerMgr::IGetLayerList](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ILayerMgr~IGetLayerList.html) to determine the size of the array.

## See Also

[ILayerMgr Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILayerMgr.html)
[ILayerMgr Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILayerMgr_members.html)

## Availability

SOLIDWORKS 99, datecode 1999207
