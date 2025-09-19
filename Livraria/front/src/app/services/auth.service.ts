import { Injectable } from "@angular/core";
import { HttpClient } from "@angular/common/http";
import { Observable,tap } from "rxjs";
import { enviroment } from "../enviroments/enviroments";


type TokenPair = {access: string; refresh?: string}

const storage ={
    get: (k:string => {typeof localStorage != null})
}