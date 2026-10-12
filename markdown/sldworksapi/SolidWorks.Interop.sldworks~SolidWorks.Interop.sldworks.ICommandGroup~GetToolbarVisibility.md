---
title: "GetToolbarVisibility Method (ICommandGroup)"
project: "SOLIDWORKS API Help"
interface: "ICommandGroup"
member: "GetToolbarVisibility"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandGroup~GetToolbarVisibility.html"
---

# GetToolbarVisibility Method (ICommandGroup)

Gets whether this toolbar is visible.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetToolbarVisibility( _
   ByVal SwContext As System.Integer _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ICommandGroup
Dim SwContext As System.Integer
Dim value As System.Boolean

value = instance.GetToolbarVisibility(SwContext)
```

### C#

```csharp
System.bool GetToolbarVisibility(
   System.int SwContext
)
```

### C++/CLI

```cpp
System.bool GetToolbarVisibility(
   System.int SwContext
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `SwContext`: Context in which to show or hide toolbar as defined in [swDocumentTypes_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swDocumentTypes_e.html)

### Return Value

True to show the toolbar, false to hide it

## VBA Syntax

See [CommandGroup::GetToolbarVisibility](ms-its:sldworksapivb6.chm::/sldworks~CommandGroup~GetToolbarVisibility.html).

## See Also

[ICommandGroup Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandGroup.html)
[ICommandGroup Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandGroup_members.html)
[ICommandGroup::SetToolbarVisibility Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandGroup~SetToolbarVisibility.html)
[ICommandGroup::HasToolbar Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandGroup~HasToolbar.html)

## Availability

SOLIDWORKS 2009 FCS, Revision Number 17.0
