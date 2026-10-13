---
title: "IGetLayerList Method (ILayerMgr)"
project: "SOLIDWORKS API Help"
interface: "ILayerMgr"
member: "IGetLayerList"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILayerMgr~IGetLayerList.html"
---

# IGetLayerList Method (ILayerMgr)

Gets a list of layers in this drawing document.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetLayerList() As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As ILayerMgr
Dim value As System.String

value = instance.IGetLayerList()
```

### C#

```csharp
System.string IGetLayerList()
```

### C++/CLI

```cpp
System.String^ IGetLayerList();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

- in-process, unmanaged C++: Pointer to an array of strings containing the name of each [ILayer](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ILayer.html) object in this [ILayerMgr](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ILayerMgr.html) object

VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## Remarks

This is a 0-based array (first element is at position 0).

Call [ILayerMgr::GetCount](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ILayerMgr~GetCount.html) to determine the size of the array.

## See Also

[ILayerMgr Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILayerMgr.html)
[ILayerMgr Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILayerMgr_members.html)
[ILayerMgr::GetLayerList Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILayerMgr~GetLayerList.html)

## Availability

SOLIDWORKS 99, datecode 1999207
