---
title: "Size Property (IAdvancedHoleElementData)"
project: "SOLIDWORKS API Help"
interface: "IAdvancedHoleElementData"
member: "Size"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAdvancedHoleElementData~Size.html"
---

# Size Property (IAdvancedHoleElementData)

Gets or sets the size of this Advanced Hole element.

## Syntax

### Visual Basic (Declaration)

```vb
Property Size As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IAdvancedHoleElementData
Dim value As System.String

instance.Size = value

value = instance.Size
```

### C#

```csharp
System.string Size {get; set;}
```

### C++/CLI

```cpp
property System.String^ Size {
   System.String^ get();
   void set (    System.String^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Size specific to the type of hole element

## VBA Syntax

See [AdvancedHoleElementData::Size](ms-its:sldworksapivb6.chm::/sldworks~AdvancedHoleElementData~Size.html).

## Examples

See the [IAdvancedHoleElementData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAdvancedHoleElementData.html) examples.

## Remarks

The size must be appropriate for the [IAdvancedHoleElementData::FastenerType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAdvancedHoleElementData~FastenerType.html).

Valid sizes are listed in the Element Specification section of the Advanced Hole PropertyManager. Select a type from the Type dropdown and inspect the Size dropdown for valid sizes.

## See Also

[IAdvancedHoleElementData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAdvancedHoleElementData.html)
[IAdvancedHoleElementData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAdvancedHoleElementData_members.html)

## Availability

SOLIDWORKS 2018 FCS, Revision Number 26.0
