---
title: "RemoveToolbar2 Method (ISldWorks)"
project: "SOLIDWORKS API Help"
interface: "ISldWorks"
member: "RemoveToolbar2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~RemoveToolbar2.html"
---

# RemoveToolbar2 Method (ISldWorks)

Removes a toolbar created with [ISldWorks::AddToolbar5](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~AddToolbar5.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function RemoveToolbar2( _
   ByVal Cookie As System.Integer, _
   ByVal ToolbarId As System.Integer _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISldWorks
Dim Cookie As System.Integer
Dim ToolbarId As System.Integer
Dim value As System.Boolean

value = instance.RemoveToolbar2(Cookie, ToolbarId)
```

### C#

```csharp
System.bool RemoveToolbar2(
   System.int Cookie,
   System.int ToolbarId
)
```

### C++/CLI

```cpp
System.bool RemoveToolbar2(
   System.int Cookie,
   System.int ToolbarId
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Cookie`: Resource ID of the toolbar; this is the same cookie that you specified in [ISwAddin::ConnectToSW](ms-its:swpublishedapi.chm::/SOLIDWORKS.Interop.swpublished~SOLIDWORKS.Interop.swpublished.ISwAddin~ConnectToSW.html)
- `ToolbarId`: Toolbar ID

### Return Value

True if the toolbar is removed, false if not

## VBA Syntax

See [SldWorks::RemoveToolbar2](ms-its:sldworksapivb6.chm::/sldworks~SldWorks~RemoveToolbar2.html).

## Remarks

If the SOLIDWORKS Design application is exiting and your application is still added-in, then you should not call this method. You should, however, clean up all other items such as the Cbitmap objects, which allows your toolbar to get reloaded in the same position next time you start the SOLIDWORKS Design application.

## See Also

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.html)
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.html)
[ISldWorks::DragToolbarButton Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~DragToolbarButton.html)
[ISldWorks::HideToolbar2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~HideToolbar2.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
