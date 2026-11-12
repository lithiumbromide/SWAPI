---
title: "DisplayWindowFromHandlex64 Method (IModelViewManager)"
project: "SOLIDWORKS API Help"
interface: "IModelViewManager"
member: "DisplayWindowFromHandlex64"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager~DisplayWindowFromHandlex64.html"
---

# DisplayWindowFromHandlex64 Method (IModelViewManager)

Displays a .NET control in this model view on 64-bit machines.

## Syntax

### Visual Basic (Declaration)

```vb
Function DisplayWindowFromHandlex64( _
   ByVal Name As System.String, _
   ByVal WindowHandle As System.Long, _
   ByVal SplitWindow As System.Boolean _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IModelViewManager
Dim Name As System.String
Dim WindowHandle As System.Long
Dim SplitWindow As System.Boolean
Dim value As System.Boolean

value = instance.DisplayWindowFromHandlex64(Name, WindowHandle, SplitWindow)
```

### C#

```csharp
System.bool DisplayWindowFromHandlex64(
   System.string Name,
   System.long WindowHandle,
   System.bool SplitWindow
)
```

### C++/CLI

```cpp
System.bool DisplayWindowFromHandlex64(
   System.String^ Name,
   System.int64 WindowHandle,
   System.bool SplitWindow
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Name`: User-defined label that appears on the tab
- `WindowHandle`: 64-bit handle of the .NET control
- `SplitWindow`: True to add a splitter window, false to not

### Return Value

True if .NET control is created, false if not

## VBA Syntax

See [ModelViewManager::DisplayWindowFromHandlex64](ms-its:sldworksapivb6.chm::/sldworks~ModelViewManager~DisplayWindowFromHandlex64.html).

## Examples

[Add .NET Controls to SOLIDWORKS using an Add-in (C#)](Add_.NET_Controls_to_SOLIDWORKS_Using_an_Add-in_Example_CSharp.htm)
[Add .NET Controls to SOLIDWORKS using an Add-in (VB.NET)](Add_.NET_Controls_to_SolidWorks_Using_an_Add-in_Example_VBNET.htm)

## Remarks

This method is only available through early binding and with 64-bit versions of the SOLIDWORKS software.

## See Also

[IModelViewManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager.html)
[IModelViewManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager_members.html)
[IModelViewManager::CreateFeatureMgrWindowFromHandlex64 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager~CreateFeatureMgrWindowFromHandlex64.html)

## Availability

SOLIDWORKS 2011 FCS, Revision Number 19.0
