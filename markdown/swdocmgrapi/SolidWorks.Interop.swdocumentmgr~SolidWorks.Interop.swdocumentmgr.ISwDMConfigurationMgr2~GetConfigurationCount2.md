---
title: "GetConfigurationCount2 Method (ISwDMConfigurationMgr2)"
project: "SOLIDWORKS Document Manager API Help"
interface: "ISwDMConfigurationMgr2"
member: "GetConfigurationCount2"
kind: "method"
source: "swdocmgrapi/SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfigurationMgr2~GetConfigurationCount2.html"
---

# GetConfigurationCount2 Method (ISwDMConfigurationMgr2)

Gets the number of configurations in this document.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetConfigurationCount2( _
   ByRef result As SwDMConfigurationError _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ISwDMConfigurationMgr2
Dim result As SwDMConfigurationError
Dim value As System.Integer

value = instance.GetConfigurationCount2(result)
```

### C#

```csharp
System.int GetConfigurationCount2(
   out SwDMConfigurationError result
)
```

### C++/CLI

```cpp
System.int GetConfigurationCount2(
   [Out] SwDMConfigurationError result
)
```

### Parameters

- `result`: Return code as defined in [swDMConfigurationError](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.SwDMConfigurationError.html)

### Return Value

Number of configurations

## VBA Syntax

See [SwDMConfigurationMgr2::GetConfigurationCount2](ms-its:swdocmgrapivb6.chm::/swdocumentmgr~SwDMConfigurationMgr2~GetConfigurationCount2.html).

## Examples

See the [ISwDMConfigurationMgr2](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfigurationMgr2.html) examples.

## See Also

[ISwDMConfigurationMgr2 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfigurationMgr2.html)
[ISwDMConfigurationMgr2 Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfigurationMgr2_members.html)

## Availability

SOLIDWORKS Document Manager API 2019 SP0
