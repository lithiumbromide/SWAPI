---
title: "COM vs. Dispatch"
project: ""
interface: ""
member: ""
kind: "topic"
source: "sldworksapiprogguide/Overview/COM_vs_Dispatch.htm"
---

# COM vs. Dispatch

SOLIDWORKS exposes its API functionality through standard COM objects. For OLE automation, the API is exposed using IDispatch.

COM implementations provide:

- Your application direct access to the underlying objects or arrays, and, subsequently, increased performance.
- Slightly more functionality and also [return an HRESULT](Return_Values.htm) value for each API call.

The COM interface is recommended for all add-in DLL projects. For executable (.exe) implementations, you can use the COM interface unless the method or property passes an array. In this case, use the equivalent Dispatch method that uses a VARIANT to encapsulate the array.
