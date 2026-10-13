---
title: "ImportCThread Property (IDerivedPartFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IDerivedPartFeatureData"
member: "ImportCThread"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDerivedPartFeatureData~ImportCThread.html"
---

# ImportCThread Property (IDerivedPartFeatureData)

Gets or sets whether to import [cosmetic threads](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICThread.html) with the derived part feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property ImportCThread As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IDerivedPartFeatureData
Dim value As System.Boolean

instance.ImportCThread = value

value = instance.ImportCThread
```

### C#

```csharp
System.bool ImportCThread {get; set;}
```

### C++/CLI

```cpp
property System.bool ImportCThread {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to import its cosmetics threads, false not not

## VBA Syntax

See [DerivedPartFeatureData::ImportCThread](ms-its:sldworksapivb6.chm::/sldworks~DerivedPartFeatureData~ImportCThread.html).

## See Also

[IDerivedPartFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDerivedPartFeatureData.html)
[IDerivedPartFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDerivedPartFeatureData_members.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
