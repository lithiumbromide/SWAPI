---
title: "CopyCustomProperties Property (ISaveBodyFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ISaveBodyFeatureData"
member: "CopyCustomProperties"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISaveBodyFeatureData~CopyCustomProperties.html"
---

# CopyCustomProperties Property (ISaveBodyFeatureData)

Gets or sets whether to copy custom properties to the new parts.

## Syntax

### Visual Basic (Declaration)

```vb
Property CopyCustomProperties As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISaveBodyFeatureData
Dim value As System.Boolean

instance.CopyCustomProperties = value

value = instance.CopyCustomProperties
```

### C#

```csharp
System.bool CopyCustomProperties {get; set;}
```

### C++/CLI

```cpp
property System.bool CopyCustomProperties {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

See **Remarks**

## VBA Syntax

See [SaveBodyFeatureData::CopyCustomProperties](ms-its:sldworksapivb6.chm::/sldworks~SaveBodyFeatureData~CopyCustomProperties.html).

## Remarks

**For VBA, .NET:**

True to copy custom properties to the new parts, false to not.

**For C++:**

VARIANT_TRUE (-1) to copy custom properties to the new parts, VARIANT_FALSE (0) to not.

## See Also

[ISaveBodyFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISaveBodyFeatureData.html)
[ISaveBodyFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISaveBodyFeatureData_members.html)

## Availability

SOLIDWORKS 2009 FCS, Revision Number 17.0
