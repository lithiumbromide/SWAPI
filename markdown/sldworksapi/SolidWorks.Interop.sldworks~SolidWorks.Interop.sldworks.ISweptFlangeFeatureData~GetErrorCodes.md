---
title: "GetErrorCodes Method (ISweptFlangeFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ISweptFlangeFeatureData"
member: "GetErrorCodes"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweptFlangeFeatureData~GetErrorCodes.html"
---

# GetErrorCodes Method (ISweptFlangeFeatureData)

Gets the error conditions that occur during swept flange feature creation or modification.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetErrorCodes() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ISweptFlangeFeatureData
Dim value As System.Integer

value = instance.GetErrorCodes()
```

### C#

```csharp
System.int GetErrorCodes()
```

### C++/CLI

```cpp
System.int GetErrorCodes();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Error codes as defined by [swSweptFlangeError_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swSweptFlangeError_e.html)

## VBA Syntax

See [SweptFlangeFeatureData::GetErrorCodes](ms-its:sldworksapivb6.chm::/sldworks~SweptFlangeFeatureData~GetErrorCodes.html).

## Examples

See the [ISheetMetalGaugeTableParameters](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheetMetalGaugeTableParameters.html) examples.

## See Also

[ISweptFlangeFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweptFlangeFeatureData.html)
[ISweptFlangeFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweptFlangeFeatureData_members.html)

## Availability

SOLIDWORKS 2021 FCS, Revision Number 29
