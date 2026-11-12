---
title: "IsX64 Method (ISwHtmlInterface)"
project: "SOLIDWORKS HTML Control Type Library"
interface: "ISwHtmlInterface"
member: "IsX64"
kind: "method"
source: "swhtmlcontrolapi/SolidWorks.Interop.swhtmlcontrol~SolidWorks.Interop.swhtmlcontrol.ISwHtmlInterface~IsX64.html"
---

# IsX64 Method (ISwHtmlInterface)

Gets whether you are running SOLIDWORKS (32-bit) or SOLIDWORKS x64 (64-bit).

## Syntax

### Visual Basic (Declaration)

```vb
Function IsX64() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ISwHtmlInterface
Dim value As System.Integer

value = instance.IsX64()
```

### C#

```csharp
System.int IsX64()
```

### C++/CLI

```cpp
System.int IsX64();
```

### Return Value

TRUE if you are running SOLIDWORKS x64, FALSE if not

## VBA Syntax

See [SwHtmlInterface::IsX64](ms-its:swhtmlcontrolapivb6.chm::/SWHTMLCONTROLLib~SwHtmlInterface~IsX64.html).

## Remarks

| If running... | Then this method returns... |
| --- | --- |
| SOLIDWORKS on 32-bit machine | FALSE |
| SOLIDWORKS on a 64-bit machine | FALSE |
| SOLIDWORKS x64 on a 64-bit machine | TRUE |

## See Also

[ISwHtmlInterface Interface](SolidWorks.Interop.swhtmlcontrol~SolidWorks.Interop.swhtmlcontrol.ISwHtmlInterface.html)
[ISwHtmlInterface Members](SolidWorks.Interop.swhtmlcontrol~SolidWorks.Interop.swhtmlcontrol.ISwHtmlInterface_members.html)

## Availability

SOLIDWORKS 2006 SP3, Revision Number 14.3
