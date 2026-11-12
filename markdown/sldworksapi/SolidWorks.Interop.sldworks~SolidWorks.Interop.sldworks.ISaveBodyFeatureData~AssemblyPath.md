---
title: "AssemblyPath Property (ISaveBodyFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ISaveBodyFeatureData"
member: "AssemblyPath"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISaveBodyFeatureData~AssemblyPath.html"
---

# AssemblyPath Property (ISaveBodyFeatureData)

Gets or sets the path and filename of the assembly (*.**sldasm**) of save bodies.

## Syntax

### Visual Basic (Declaration)

```vb
Property AssemblyPath As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As ISaveBodyFeatureData
Dim value As System.String

instance.AssemblyPath = value

value = instance.AssemblyPath
```

### C#

```csharp
System.string AssemblyPath {get; set;}
```

### C++/CLI

```cpp
property System.String^ AssemblyPath {
   System.String^ get();
   void set (    System.String^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Path and filename of the assembly (*.**sldasm**) of save bodies

## VBA Syntax

See [SaveBodyFeatureData::AssemblyPath](ms-its:sldworksapivb6.chm::/sldworks~SaveBodyFeatureData~AssemblyPath.html).

## See Also

[ISaveBodyFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISaveBodyFeatureData.html)
[ISaveBodyFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISaveBodyFeatureData_members.html)

## Availability

SOLIDWORKS 2009 FCS, Revision Number 17.0
