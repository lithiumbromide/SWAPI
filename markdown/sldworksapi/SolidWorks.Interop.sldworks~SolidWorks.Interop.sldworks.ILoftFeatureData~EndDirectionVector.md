---
title: "EndDirectionVector Property (ILoftFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ILoftFeatureData"
member: "EndDirectionVector"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoftFeatureData~EndDirectionVector.html"
---

# EndDirectionVector Property (ILoftFeatureData)

Gets or sets the direction vector in which to end this loft feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property EndDirectionVector As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ILoftFeatureData
Dim value As System.Object

instance.EndDirectionVector = value

value = instance.EndDirectionVector
```

### C#

```csharp
System.object EndDirectionVector {get; set;}
```

### C++/CLI

```cpp
property System.Object^ EndDirectionVector {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

End direction vector

## VBA Syntax

See [LoftFeatureData::EndDirectionVector](ms-its:sldworksapivb6.chm::/sldworks~LoftFeatureData~EndDirectionVector.html).

## Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this property.

## See Also

[ILoftFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoftFeatureData.html)
[ILoftFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoftFeatureData_members.html)
[ILoftFeatureData::StartDirectionVector Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoftFeatureData~StartDirectionVector.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
