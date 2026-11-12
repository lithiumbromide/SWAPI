---
title: "AddContextMenuFlyout Method (IFlyoutGroup)"
project: "SOLIDWORKS API Help"
interface: "IFlyoutGroup"
member: "AddContextMenuFlyout"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFlyoutGroup~AddContextMenuFlyout.html"
---

# AddContextMenuFlyout Method (IFlyoutGroup)

Adds this flyout to the context menus of the specified documents and selections.

## Syntax

### Visual Basic (Declaration)

```vb
Function AddContextMenuFlyout( _
   ByVal DocumentType As System.Integer, _
   ByVal SelectionType As System.Integer _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IFlyoutGroup
Dim DocumentType As System.Integer
Dim SelectionType As System.Integer
Dim value As System.Boolean

value = instance.AddContextMenuFlyout(DocumentType, SelectionType)
```

### C#

```csharp
System.bool AddContextMenuFlyout(
   System.int DocumentType,
   System.int SelectionType
)
```

### C++/CLI

```cpp
System.bool AddContextMenuFlyout(
   System.int DocumentType,
   System.int SelectionType
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `DocumentType`: Type of document as defined in [swDocumentTypes_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swDocumentTypes_e.html)
- `SelectionType`: Type of object as defined in [swSelectType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swSelectType_e.html)

### Return Value

True if successful, false if not

## VBA Syntax

See [FlyoutGroup::AddContextMenuFlyout](ms-its:sldworksapivb6.chm::/sldworks~FlyoutGroup~AddContextMenuFlyout.html).

## Examples

[Create Flyouts in the CommandManager (C#)](Create_Flyouts_in_the_CommandManager_Example_CSharp.htm)
[Create Flyouts in the CommandManager (VB.NET)](Create_Flyouts_in_the_CommandManager_Example_VBNET.htm)

## Remarks

Call this method once for each set of DocumentType and SelectionType parameters.

Context-sensitive menus support only the standard flyout style ([swCommandFlyoutStyle_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swCommandFlyoutStyle_e.html).swCommandFlyoutStyle_Simple), in which there is no immediate action on the main flyout button.

## See Also

[IFlyoutGroup Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFlyoutGroup.html)
[IFlyoutGroup Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFlyoutGroup_members.html)

## Availability

SOLIDWORKS 2011 FCS, Revision Number 19.0
