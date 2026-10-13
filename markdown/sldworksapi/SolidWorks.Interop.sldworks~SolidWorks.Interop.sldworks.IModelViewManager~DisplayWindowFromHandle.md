---
title: "DisplayWindowFromHandle Method (IModelViewManager)"
project: "SOLIDWORKS API Help"
interface: "IModelViewManager"
member: "DisplayWindowFromHandle"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager~DisplayWindowFromHandle.html"
---

# DisplayWindowFromHandle Method (IModelViewManager)

Obsolete. Superseded by [IModelViewManager::DisplayWindowFromHandlex64](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager~DisplayWindowFromHandlex64.html).

This method is unsafe to use with 64-bit SOLIDWORKS, i.e. all versions since SOLIDWORKS 2016.

The 32-bit integer returned may be to small to contain the 64-bit window handle/pointer, and will be truncated silently. A critical exception will occur sometime later, when the truncated handle/pointer is used.

Displays a .NET control in this model view.

## Syntax

### Visual Basic (Declaration)

```vb
Function DisplayWindowFromHandle( _
   ByVal Name As System.String, _
   ByVal WindowHandle As System.Integer, _
   ByVal SplitWindow As System.Boolean _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IModelViewManager
Dim Name As System.String
Dim WindowHandle As System.Integer
Dim SplitWindow As System.Boolean
Dim value As System.Boolean

value = instance.DisplayWindowFromHandle(Name, WindowHandle, SplitWindow)
```

### C#

```csharp
System.bool DisplayWindowFromHandle(
   System.string Name,
   System.int WindowHandle,
   System.bool SplitWindow
)
```

### C++/CLI

```cpp
System.bool DisplayWindowFromHandle(
   System.String^ Name,
   System.int WindowHandle,
   System.bool SplitWindow
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Name`: User-defined label that appears on the tab
- `WindowHandle`: Handle of the .NET control
- `SplitWindow`: True to add a splitter window, false to not

### Return Value

True if .NET control is created, false if not

## VBA Syntax

See [ModelViewManager::DisplayWindowFromHandle](ms-its:sldworksapivb6.chm::/sldworks~ModelViewManager~DisplayWindowFromHandle.html).

## Remarks

**All applications are required to be compatible with SOLIDWORKS x64. You must replace all calls to 32-bit only APIs with calls to their 64-bit safe counterparts.**

See [Eliminating 32-bit only API use](sldworksapiprogguide.chm::/Overview/Eliminating_32-Bit_Only_API_Use.htm) for more information.

## See Also

[IModelViewManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager.html)
[IModelViewManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager_members.html)
[IModelViewManager::CreateFeatureMgrWindowFromHandle Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager~CreateFeatureMgrWindowFromHandle.html)

## Availability

SOLIDWORKS 2011 FCS, Revision Number 19.0
