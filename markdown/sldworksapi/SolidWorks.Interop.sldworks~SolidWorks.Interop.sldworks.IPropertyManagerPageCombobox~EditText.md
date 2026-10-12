---
title: "EditText Property (IPropertyManagerPageCombobox)"
project: "SOLIDWORKS API Help"
interface: "IPropertyManagerPageCombobox"
member: "EditText"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageCombobox~EditText.html"
---

# EditText Property (IPropertyManagerPageCombobox)

Gets or sets the text in the combo box.

## Syntax

### Visual Basic (Declaration)

```vb
Property EditText As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IPropertyManagerPageCombobox
Dim value As System.String

instance.EditText = value

value = instance.EditText
```

### C#

```csharp
System.string EditText {get; set;}
```

### C++/CLI

```cpp
property System.String^ EditText {
   System.String^ get();
   void set (    System.String^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Text for or in combo box

## VBA Syntax

See [PropertyManagerPageCombobox::EditText](ms-its:sldworksapivb6.chm::/sldworks~PropertyManagerPageCombobox~EditText.html).

## Remarks

[IPropertyManagerPageCombobox::Style](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IPropertyManagerPageCombobox~Style.html) must be set to swPropMgrPageComboBoxStyle_EditableText to edit text in a combo box.

## See Also

[IPropertyManagerPageCombobox Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageCombobox.html)
[IPropertyManagerPageCombobox Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageCombobox_members.html)

## Availability

SOLIDWORKS 2007 FCS, Revision Number 15.0
