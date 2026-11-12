---
title: "ReplaceCommandItem Method (IFlyoutGroup)"
project: "SOLIDWORKS API Help"
interface: "IFlyoutGroup"
member: "ReplaceCommandItem"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFlyoutGroup~ReplaceCommandItem.html"
---

# ReplaceCommandItem Method (IFlyoutGroup)

Replaces a command item at the specified position.

## Syntax

### Visual Basic (Declaration)

```vb
Function ReplaceCommandItem( _
   ByVal Position As System.Integer, _
   ByVal Name As System.String, _
   ByVal HintString As System.String, _
   ByVal ImageListIndex As System.Integer, _
   ByVal CallbackFunction As System.String, _
   ByVal UpdateCallbackFunction As System.String _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IFlyoutGroup
Dim Position As System.Integer
Dim Name As System.String
Dim HintString As System.String
Dim ImageListIndex As System.Integer
Dim CallbackFunction As System.String
Dim UpdateCallbackFunction As System.String
Dim value As System.Integer

value = instance.ReplaceCommandItem(Position, Name, HintString, ImageListIndex, CallbackFunction, UpdateCallbackFunction)
```

### C#

```csharp
System.int ReplaceCommandItem(
   System.int Position,
   System.string Name,
   System.string HintString,
   System.int ImageListIndex,
   System.string CallbackFunction,
   System.string UpdateCallbackFunction
)
```

### C++/CLI

```cpp
System.int ReplaceCommandItem(
   System.int Position,
   System.String^ Name,
   System.String^ HintString,
   System.int ImageListIndex,
   System.String^ CallbackFunction,
   System.String^ UpdateCallbackFunction
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Position`: 0-based index of the item to replace in the flyout
- `Name`: Name of the item to add to the flyout
- `HintString`: Text displayed in the SOLIDWORKS Design status bar when the pointer is on the item
- `ImageListIndex`: Index of the image in the icon list assigned to the parent flyout (see **Remarks**)
- `CallbackFunction`: Function to call when this item is selected
- `UpdateCallbackFunction`: Optional function that controls the state of the item; if specified, then SOLIDWORKS Design calls this function before displaying the item

  | If your method returns... | Then SOLIDWORKS Design... |
  | --- | --- |
  | 0 | Deselects and disables the item |
  | 1 | Deselects and enables the item; this is the default state if no update function is specified |
  | 2 | Selects and disables the item |
  | 3 | Selects and enables the item |
  | 4 | Hides the item |

## VBA Syntax

See [FlyoutGroup::ReplaceCommandItem](ms-its:sldworksapivb6.chm::/sldworks~FlyoutGroup~ReplaceCommandItem.html).

## Remarks

ImageListIndex is 0-based. The size of the index is equal to the number of images in the large or small graphic file for that flyout. See [IFlyoutGroup::LargeIconList](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFlyoutGroup~LargeIconList.html) and [IFlyoutGroup::SmallIconList](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFlyoutGroup~SmallIconList.html) for details.

You can use -1 for ImageListIndex to specify that no icon is needed.

## See Also

[IFlyoutGroup Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFlyoutGroup.html)
[IFlyoutGroup Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFlyoutGroup_members.html)
[IFlyoutGroup::RemoveAllCommandItems Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFlyoutGroup~RemoveAllCommandItems.html)
[IFlyoutGroup::RemoveCommandItem Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFlyoutGroup~RemoveCommandItem.html)
[IFlyoutGroup::AddCommandItem Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFlyoutGroup~AddCommandItem.html)

## Availability

SOLIDWORKS 2011 FCS, Revision Number 19.0
