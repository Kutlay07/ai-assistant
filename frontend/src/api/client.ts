const BASE_URL = "http://127.0.0.1:8000/api/v1";

export async function post<T>(
    endpoint: string,
    body: unknown,
): Promise<T> {
    const response = await fetch(`${BASE_URL}${endpoint}`, {
        method: "POST",
        headers: {
            "content-Type": "application/json",
        },
        body: JSON.stringify(body),
    });

    if (!response.ok) {
        throw new Error(`Request failed: ${response.status}`);
    }

    return response.json() as Promise<T>;
}

export async function get<T>(
    endpoint: string,
): Promise<T> {

    const response = await fetch(
        `${BASE_URL}${endpoint}`,
    );

    if (!response.ok) {
        throw new Error("Request failed");
    }

    return response.json();
}