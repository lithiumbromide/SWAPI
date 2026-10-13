---
title: "Checked Property (IPropertyManagerPageOption)"
project: "SOLIDWORKS API Help"
interface: "IPropertyManagerPageOption"
member: "Checked"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageOption~Checked.html"
---

# Checked Property (IPropertyManagerPageOption)

gets or sets whether the option is selected.

## Syntax

### Visual Basic (Declaration)

```vb
Property Checked As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IPropertyManagerPageOption
Dim value As System.Boolean

instance.Checked = value

value = instance.Checked
```

### C#

```csharp
System.bool Checked {get; set;}
```

### C++/CLI

```cpp
property System.bool Checked {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True if the option is selected, false if not

## VBA Syntax

See [PropertyManagerPageOption::Checked](ms-its:sldworksapivb6.chm::/sldworks~PropertyManagerPageOption~Checked.html).

## See Also

[IPropertyManagerPageOption Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageOption.html)
[IPropertyManagerPageOption Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageOption_members.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
