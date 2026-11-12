---
title: "ImportSurf Property (IDerivedPartFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IDerivedPartFeatureData"
member: "ImportSurf"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDerivedPartFeatureData~ImportSurf.html"
---

# ImportSurf Property (IDerivedPartFeatureData)

Gets or sets whether to import surface bodies with the derived part feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property ImportSurf As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IDerivedPartFeatureData
Dim value As System.Boolean

instance.ImportSurf = value

value = instance.ImportSurf
```

### C#

```csharp
System.bool ImportSurf {get; set;}
```

### C++/CLI

```cpp
property System.bool ImportSurf {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to import its surface bodies, false to not

## VBA Syntax

See [DerivedPartFeatureData::ImportSurf](ms-its:sldworksapivb6.chm::/sldworks~DerivedPartFeatureData~ImportSurf.html).

## See Also

[IDerivedPartFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDerivedPartFeatureData.html)
[IDerivedPartFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDerivedPartFeatureData_members.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
