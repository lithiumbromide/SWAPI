---
title: "StartDirectionVector Property (ILoftFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ILoftFeatureData"
member: "StartDirectionVector"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoftFeatureData~StartDirectionVector.html"
---

# StartDirectionVector Property (ILoftFeatureData)

Gets or sets the direction vector in which to start this loft feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property StartDirectionVector As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ILoftFeatureData
Dim value As System.Object

instance.StartDirectionVector = value

value = instance.StartDirectionVector
```

### C#

```csharp
System.object StartDirectionVector {get; set;}
```

### C++/CLI

```cpp
property System.Object^ StartDirectionVector {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Start direction vector

## VBA Syntax

See [LoftFeatureData::StartDirectionVector](ms-its:sldworksapivb6.chm::/sldworks~LoftFeatureData~StartDirectionVector.html).

## Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this property.

## See Also

[ILoftFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoftFeatureData.html)
[ILoftFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoftFeatureData_members.html)
[ILoftFeatureData::EndDirectionVector Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoftFeatureData~EndDirectionVector.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
