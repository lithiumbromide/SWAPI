---
title: "Select4 Method (IComponent2)"
project: "SOLIDWORKS API Help"
interface: "IComponent2"
member: "Select4"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~Select4.html"
---

# Select4 Method (IComponent2)

Selects this component.

## Syntax

### Visual Basic (Declaration)

```vb
Function Select4( _
   ByVal Append As System.Boolean, _
   ByVal Data As SelectData, _
   ByVal ShowPopup As System.Boolean _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IComponent2
Dim Append As System.Boolean
Dim Data As SelectData
Dim ShowPopup As System.Boolean
Dim value As System.Boolean

value = instance.Select4(Append, Data, ShowPopup)
```

### C#

```csharp
System.bool Select4(
   System.bool Append,
   SelectData Data,
   System.bool ShowPopup
)
```

### C++/CLI

```cpp
System.bool Select4(
   System.bool Append,
   SelectData^ Data,
   System.bool ShowPopup
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Append`: True appends the selection to the selection list, false replaces the selection list
- `Data`: Pointer to the [ISelectData](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISelectData.html) object
- `ShowPopup`: True to show shortcut menu, false to not

### Return Value

True if the component is selected, false if not

## VBA Syntax

See [Component2::Select4](ms-its:sldworksapivb6.chm::/sldworks~Component2~Select4.html).

## Examples

[Fire Notifications When Renaming Components (C#)](Fire_Notifications_When_Renaming_Components_Example_CSharp.htm)
[Fire Notifications When Renaming Components (VB.NET)](Fire_Notifications_When_Renaming_Components_Example_VBNET.htm)
[Fire Notifications When Renaming Components (VBA)](Fire_Notifications_When_Renaming_Components_Example_VB.htm)

## See Also

[IComponent2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2.html)
[IComponent2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2_members.html)
[ISelectionMgr::GetSelectedObjectsComponent3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~GetSelectedObjectsComponent3.html)
[IModelDocExtension::SelectAll Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SelectAll.html)
[IComponent2::DeSelect Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~DeSelect.html)

## Availability

SOLIDWORKS 2009 FCS, Revision Number 17
