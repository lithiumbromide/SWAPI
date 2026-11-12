---
title: "ConsumeBody Property (ISaveBodyFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ISaveBodyFeatureData"
member: "ConsumeBody"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISaveBodyFeatureData~ConsumeBody.html"
---

# ConsumeBody Property (ISaveBodyFeatureData)

Gets or sets whether to consume all bodies in the original part.

## Syntax

### Visual Basic (Declaration)

```vb
Property ConsumeBody As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISaveBodyFeatureData
Dim value As System.Boolean

instance.ConsumeBody = value

value = instance.ConsumeBody
```

### C#

```csharp
System.bool ConsumeBody {get; set;}
```

### C++/CLI

```cpp
property System.bool ConsumeBody {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

See **Remarks**

## VBA Syntax

See [SaveBodyFeatureData::ConsumeBody](ms-its:sldworksapivb6.chm::/sldworks~SaveBodyFeatureData~ConsumeBody.html).

## Remarks

**For VBA, .NET:**

True to consume all bodies in the original part, false to not.

**For C++:**

VARIANT_TRUE (-1) to consume all bodies in the original part, VARIANT_FALSE (0) to not.

## See Also

[ISaveBodyFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISaveBodyFeatureData.html)
[ISaveBodyFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISaveBodyFeatureData_members.html)

## Availability

SOLIDWORKS 2009 FCS, Revision Number 17.0
