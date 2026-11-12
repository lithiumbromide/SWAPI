---
title: "GetImportedBody Method (ISwDMConfiguration3)"
project: "SOLIDWORKS Document Manager API Help"
interface: "ISwDMConfiguration3"
member: "GetImportedBody"
kind: "method"
source: "swdocmgrapi/SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration3~GetImportedBody.html"
---

# GetImportedBody Method (ISwDMConfiguration3)

Gets the imported solid body in this configuration and writes the body to the specified file in Parasolid .x_b format.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetImportedBody( _
   ByVal index As System.Integer, _
   ByVal fileName As System.String _
) As SwDmBodyError
```

### Visual Basic (Usage)

```vb
Dim instance As ISwDMConfiguration3
Dim index As System.Integer
Dim fileName As System.String
Dim value As SwDmBodyError

value = instance.GetImportedBody(index, fileName)
```

### C#

```csharp
SwDmBodyError GetImportedBody(
   System.int index,
   System.string fileName
)
```

### C++/CLI

```cpp
SwDmBodyError GetImportedBody(
   System.int index,
   System.String^ fileName
)
```

### Parameters

- `index`: Number indicating which imported solid body in this configuration to get
- `fileName`: File to which to write the body in Parasolid .x_b format (see Remarks)

### Return Value

Success or error code as defined by [SwDmBodyError](SOLIDWORKS.Interop.swdocumentmgr~SOLIDWORKS.Interop.swdocumentmgr.SwDmBodyError.html)

## VBA Syntax

See [SwDMConfiguration3::GetImportedBody](ms-its:swdocmgrapivb6.chm::/swdocumentmgr~SwDMConfiguration3~GetImportedBody.html).

## Remarks

This method gets imported solid bodies only; it does not get imported surface bodies.

Before calling this method, call [ISwConfiguration3::GetImportedBodiesCount](SOLIDWORKS.Interop.swdocumentmgr~SOLIDWORKS.Interop.swdocumentmgr.ISwDMConfiguration3~GetImportedBodiesCount.html) to get the number of imported solid bodies in the configuration.

| If fileName... | Then this method... |
| --- | --- |
| Exists | Writes the imported solid body to fileName in Parasolid .x_b format, overwriting any data in that file |
| Does not exist | Creates fileName and writes the imported solid body to that file in Parasolid .x_b format |

## See Also

[ISwDMConfiguration3 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration3.html)
[ISwDMConfiguration3 Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration3_members.html)

## Availability

SOLIDWORKS Document Manager API 2004 SP2
