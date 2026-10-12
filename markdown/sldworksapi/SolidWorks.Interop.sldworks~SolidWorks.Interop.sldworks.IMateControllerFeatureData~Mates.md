---
title: "Mates Property (IMateControllerFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IMateControllerFeatureData"
member: "Mates"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMateControllerFeatureData~Mates.html"
---

# Mates Property (IMateControllerFeatureData)

Gets or sets the mates in this mate controller.

## Syntax

### Visual Basic (Declaration)

```vb
Property Mates As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IMateControllerFeatureData
Dim value As System.Object

instance.Mates = value

value = instance.Mates
```

### C#

```csharp
System.object Mates {get; set;}
```

### C++/CLI

```cpp
property System.Object^ Mates {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Array of supportive [mates](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMate2.html)

## VBA Syntax

See [MateControllerFeatureData::Mates](ms-its:sldworksapivb6.chm::/sldworks~MateControllerFeatureData~Mates.html).

## Examples

See the [IMateControllerFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMateControllerFeatureData.html) examples.

## Remarks

This property is only valid after the mate controller is created.

To create a mate controller see the Remarks section of IMateControllerFeatureData.

## See Also

[IMateControllerFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMateControllerFeatureData.html)
[IMateControllerFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMateControllerFeatureData_members.html)

## Availability

SOLIDWORKS 2023 FCS, Revision Number 31
